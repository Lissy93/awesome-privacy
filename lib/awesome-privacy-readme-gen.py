"""
Reads app list from awesome-privacy.yml,
formats into markdown, and inserts into README.md
"""

import os
import re
import yaml
import logging
from urllib.parse import urlparse, quote

# Configure Logging
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)

# Determine the project root based on the script's location
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app_list_file_path = os.path.join(project_root, 'awesome-privacy.yml')
readme_path = os.path.join(project_root, '.github/README.md')
icon_size=16

# Read the main YAML file, where all data lives
logger.info("Reading the awesome-privacy file...")
with open(app_list_file_path, 'r') as file:
    data = yaml.safe_load(file)

def iconElement(serviceUrl, serviceIcon):
  path = serviceIcon or f"https://icon.horse/icon/{urlparse(serviceUrl).netloc}"
  return f"<img src='{path}' width='{icon_size}' height='{icon_size}' alt='icon' />"

def repoElement(repoUrl):
    if not repoUrl:
        return ""
    return (
        f"[![GitHub: {repoUrl}](https://img.shields.io/github/stars/{repoUrl}"
        f"?style=flat&logo=github&label={repoUrl.split('/')[1]}"
        "&color=%235f53f4&cacheSeconds=3600)]"
        f"(https://github.com/{repoUrl})"
    )

def tosElement(tosdrId):
    if not tosdrId:
        return ""
    return f"[![Privacy Policy](https://shields.tosdr.org/en_{tosdrId}.svg)](https://tosdr.org/en/service/{tosdrId})"

def statsElement(app, categoryName, sectionName):
    statsStr = ""
    if app.get('openSource') == True:
        github = app.get('github')
        if github:
            link = f"https://github.com/{github}"
        elif app.get('url'):
            link = app.get('url')
        else:
            link = f"https://awesome-privacy.xyz/{slugify(categoryName)}/{slugify(sectionName)}/{slugify(app.get('name'))}"
        statsStr += (
            f"[![Open Source](https://img.shields.io/badge/-Open_Source-3DA639"
            f"?style=flat&logo=opensourceinitiative&logoColor=white)]({link}) "
        )
    if app.get('securityAudited') == True:
        statsStr += (
            "![Security Audited](https://img.shields.io/badge/-Security_Audited-3DA639"
            "?style=flat&logo=data:image/svg+xml;base64,"
            "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAxTDMgNXY2YzAgNS41NSAzLjg0IDEwLjc0IDkgMTIgNS4xNi0xLjI2IDktNi40NSA5LTEyVjVsLTktNHoiLz48L3N2Zz4="
            "&logoColor=white) "
        )
    if app.get('acceptsCrypto') == True:
        statsStr += (
            "![Accepts Anonymous Payment](https://img.shields.io/badge/-Anon_Payment_Accepted"
            "%EF%B8%8F-3DA639?style=flat&logo=bitcoincash&logoColor=white) "
        )
    return statsStr

def slugify(title):
    if not title:
        return ''
    title = title.lower()
    title = re.sub(r'\s+', '-', title)
    title = re.sub(r'\+|&', 'and', title)
    title = title.replace('?', '')
    return title

def shieldsEncode(text):
    if not text: return ''
    text = text.strip().replace('-', '--').replace('_', '__').replace(' ', '_')
    return quote(text, safe='_-.')

def awesomePrivacyReport(categoryName, sectionName, serviceName):
  if not serviceName:
      return ""
  return (
      f"[![{serviceName} on Awesome Privacy]"
      f"(https://img.shields.io/badge/View%20Report-FC60A8?style=flat&logo=awesomelists&label={serviceName.replace(' ', '_')})]"
      f"(https://awesome-privacy.xyz/{slugify(categoryName)}/{slugify(sectionName)}/{slugify(serviceName)})"
  )

def playStoreBadge(name, androidApp):
    if not androidApp: return ""
    encoded = shieldsEncode(name)
    return (
        f"[![{name} on Google Play](https://img.shields.io/badge/-{encoded}-3bd47f"
        f"?style=flat&logo=android&logoColor=white)]"
        f"(https://play.google.com/store/apps/details?id={androidApp}) "
    )

def appStoreBadge(name, iosApp):
    if not iosApp: return ""
    encoded = shieldsEncode(name)
    return (
        f"[![{name} on App Store](https://img.shields.io/badge/-{encoded}-0D96F6"
        f"?style=flat&logo=appstore&logoColor=white)]"
        f"({iosApp}) "
    )

def redditBadge(subreddit):
    if not subreddit or not subreddit.strip(): return ""
    sub = subreddit.strip()
    return (
        f"[![r/{sub} on Reddit](https://img.shields.io/badge/-{sub}-FF4500"
        f"?style=flat&logo=reddit&logoColor=white)]"
        f"(https://reddit.com/r/{sub}) "
    )

def discordBadge(name, discordInvite):
    if not discordInvite or not discordInvite.strip(): return ""
    invite = discordInvite.strip()
    encoded = shieldsEncode(name)
    link = invite if invite.startswith('https://') else f"https://discord.gg/{invite}"
    return (
        f"[![{name} on Discord](https://img.shields.io/badge/-{encoded}-5865F2"
        f"?style=flat&logo=discord&logoColor=white)]"
        f"({link}) "
    )

_MD_PATTERNS = [
    re.compile(r'\[([^\]]*)\]\([^)]*\)'),    # [text](url) — group 1 = visible text
    re.compile(r'\*\*(.+?)\*\*'),             # **bold**
    re.compile(r'`([^`]+)`'),                 # `code`
    re.compile(r'(?<!\*)\*([^*]+)\*(?!\*)'),  # *italic*
]

def truncateMarkdown(text, maxLen=200):
    """Returns (truncated_text, was_truncated) preserving markdown constructs."""
    if len(text) <= maxLen:
        return text, False

    result = []
    visible = 0
    i = 0

    while i < len(text) and visible < maxLen:
        for pattern in _MD_PATTERNS:
            m = pattern.match(text, i)
            if m:
                result.append(m.group(0))
                visible += len(m.group(1))
                i = m.end()
                break
        else:
            result.append(text[i])
            visible += 1
            i += 1

    return ''.join(result).rstrip(), True

def makeHref(text):
    if not text: return "#"
    return re.sub(r'[^\w\s-]', '', text.lower()).replace(" ", "-")

def makeContents():
    contents = "<blockquote><details>\n"
    contents += "<summary>📋 <b>Contents</b></summary>\n"

    for category in data.get('categories'):
        contents += f"\n- **{category.get('name')}**"
        for section in category.get('sections'):
            contents += (
                f"\n\t- [{section.get('name')}](#{makeHref(section.get('name'))}) "
                f"({len(section.get('services') or [])})"
            )
    contents += "\n</details></blockquote>\n\n"
    return contents

def makeAwesomePrivacy():
  markdown = ""
  for category in data.get('categories'):
      markdown += f"## {category.get('name')}\n\n"
      for section in category.get('sections'):
          markdown += f"### {section.get('name')}\n\n"
          # Add intro
          if section.get('intro'):
            markdown += f"{section.get('intro')}\n"
          # No services yet
          if not section.get('services') or len(section.get('services')) == 0:
            markdown += (
              "<p  align=\"center\">"
              "<b>⚠️ This section is still a work in progress ⚠️</b><br />"
              "<i>Check back soon, or help us complete it by submitting a pull request</i>"
              "</p>"
            )
          # For each service, list it's name, icon, url, and description
          for app in section.get('services') or []:
              description, was_truncated = truncateMarkdown(app.get('description', ''))
              ap_link = (
                  f"https://awesome-privacy.xyz/"
                  f"{slugify(category.get('name'))}/{slugify(section.get('name'))}/{slugify(app.get('name'))}"
              )
              ellipsis = f"[…]({ap_link} \"View full {app.get('name')} report\")" if was_truncated else ""
              markdown += (
                  f"- **[{iconElement(app.get('url'), app.get('icon'))} {app.get('name')}]"
                  f"({app.get('url')})** - {description}{ellipsis} \n"
              )
              badges = ' '.join(filter(None, [
                  repoElement(app.get('github')),
                  tosElement(app.get('tosdrId')),
                  awesomePrivacyReport(category.get('name'), section.get('name'), app.get('name')),
                  statsElement(app, category.get('name'), section.get('name')).rstrip(),
                  playStoreBadge(app.get('name'), app.get('androidApp')).rstrip(),
                  appStoreBadge(app.get('name'), app.get('iosApp')).rstrip(),
                  redditBadge(app.get('subreddit')).rstrip(),
                  discordBadge(app.get('name'), app.get('discordInvite')).rstrip(),
              ]))
              if badges:
                  markdown += (
                      f"\t- <details>\n\t\t<summary>Stats</summary>\n\n\t\t"
                      f"{badges}ㅤ \n"
                      f"\n\t\t</details>\n"
                  )
          markdown += "\n"
          # If word of warning exists, append it
          if section.get('wordOfWarning'):
            markdown += "<details>\n<summary>⚠️ <b>Word of Warning</b></summary>\n\n"
            markdown += f"> {section.get('wordOfWarning')}\n\n"
            markdown += "</details>\n\n"
          # If notable mentions exists, append it (either as a list or a single string)
          if section.get('notableMentions'):
            markdown += "<details>\n<summary>✳️ <b>Notable Mentions</b></summary>\n\n"
            if isinstance(section.get('notableMentions'), list):
              for mention in section.get('notableMentions'):
                markdown += f"> - [{mention.get('name')}]({mention.get('url')})" + (
                  f" - {mention.get('description')}" if mention.get('description') else "\n"
              )
            else:
              notable_mentions = section.get('notableMentions').replace('\n', '\n> ')
              markdown += f"> {notable_mentions}"

            markdown += "</details>\n\n"
          # If further info exists, append it
          if section.get('furtherInfo'):
            markdown += "<details>\n<summary>ℹ️ <b>Further Info</b></summary>\n\n"
            markdown += f"> {section.get('furtherInfo')}"
            markdown += "</details>\n\n"
          markdown += "<p align=\"right\"><sup><a href=\"#top\">⬆️ [Back to Top]</a></sub></p>\n"
          markdown += "\n---\n\n"
  return markdown

awesome_privacy_results = makeContents() + makeAwesomePrivacy()

# Update the README.md between markers
logger.info("Reading README.md file...")
with open(readme_path, 'r') as file:
    readme_content = file.read()

def update_content_between_markers(content, start_marker, end_marker, new_content):
    logger.info(f"Updating content between {start_marker} and {end_marker} markers...")
    start_index = content.find(start_marker)
    end_index = content.find(end_marker)

    if start_index != -1 and end_index != -1:
        before_section = content[:start_index + len(start_marker)]
        after_section = content[end_index:]
        updated_content = before_section + '\n' + new_content + after_section
        return updated_content
    else:
        logger.error(f"Markers {start_marker} and {end_marker} not found.")
        return content

# Update guides and resources in README.md
readme_content = update_content_between_markers(
  readme_content,
  "<!-- awesome-privacy-start -->",
  "<!-- awesome-privacy-end -->",
  awesome_privacy_results
)

# Write back the updated content to README.md
logger.info("Writing back to README.md...")
with open(readme_path, 'w') as file:
    file.write(readme_content)

# All done. Time to go home for tea and medals.
logger.info("Script completed successfully!")
