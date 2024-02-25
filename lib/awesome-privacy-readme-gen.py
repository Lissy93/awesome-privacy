"""
Reads app list from awesome-privacy.yml,
formats into markdown, and inserts into README.md 
"""

import os
import re
import yaml
import logging
from urllib.parse import urlparse

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
        f"\t- [![GitHub: {repoUrl}](https://img.shields.io/github/stars/{repoUrl}"
        f"?style=flat&logo=github&label={repoUrl.split('/')[1]}"
        "&labelColor=%230d1117&color=%23302982&cacheSeconds=3600)]"
        f"(https://github.com/{repoUrl})\n"
    )

def makeHref(text):
    if not text: return "#"
    return re.sub(r'[^\w\s-]', '', text.lower()).replace(" ", "-")

def makeContents():
    contents = "<details>\n"
    contents += "<summary><h2>Contents</h2></summary>\n"

    for category in data.get('categories'):
        contents += f"\n- **{category.get('name')}**"
        for section in category.get('sections'):
            contents += (
                f"\n\t- [{section.get('name')}](#{makeHref(section.get('name'))}) "
                f"({len(section.get('services') or [])})"
            )
    contents += "\n</details>\n\n"
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
              markdown += (
                  f"- **[{iconElement(app.get('url'), app.get('icon'))} {app.get('name')}]"
                  f"({app.get('url')})** - {app.get('description')} "
                  f"{repoElement(app.get('github'))}"
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
