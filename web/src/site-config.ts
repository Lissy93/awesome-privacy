export const authorProjects = [
  {
    title: 'Email Comparison',
    description: 'Objective comparison of private/secure mail providers',
    icon: 'https://email-comparison.as93.net/favicon.png',
    link: 'https://github.com/lissy93/email-comparison',
  },
  {
    title: 'Personal Security Checklist',
    description: 'Checklist of security tips, for protecting your privacy',
    icon: 'https://i.ibb.co/Rb6P6h6/shield.png',
    link: 'https://github.com/Lissy93/personal-security-checklist',
  },
  {
    title: 'Web-Check',
    description: 'OSINT tool for analysing any website',
    icon: 'https://web-check.as93.net/web-check.png',
    link: 'https://github.com/lissy93/web-check',
  },
  {
    title: 'Dashy',
    description: 'Dashboard app, for organising your self-hosted services',
    icon: 'https://dashy.to/img/dashy.png',
    link: 'https://github.com/lissy93/dashy',
  },
  {
    title: 'Portainer-Templates',
    description: 'Compiled repository of 1-click Docker apps for self-hosting',
    icon: 'https://portainer-templates.as93.net/favicon.png',
    link: 'https://github.com/lissy93/portainer-templates',
  },
  {
    title: 'AdGuardian',
    description:
      'CLI tool for monitoring your networks traffic and AdGuard DNS stats',
    icon: 'https://adguardian.as93.net/favicon.png',
    link: 'https://github.com/lissy93/adguardian-term',
  },
  {
    title: 'Bug-Bounties',
    description:
      'Database of websites which accept responsible vulnerability disclosure',
    icon: 'https://bug-bounties.as93.net/favicon.png',
    link: 'https://github.com/lissy93/bug-bounties',
  },
  {
    title: 'Git-In',
    description: 'Tools and resources to help beginners get into open source',
    icon: 'https://www.git-in.to/favicon.png',
    link: 'https://github.com/lissy93/git-in',
  },
];

export const authorSocials = [
  {
    title: 'GitHub',
    icon: 'hub',
    link: 'https://github.com/lissy93',
    color: '#EA4AAA',
  },
  {
    title: 'Twitter',
    icon: 'twitter',
    link: 'https://x.com/lissy_sykes',
    color: '#1D9BF0',
  },
  {
    title: 'Mastodon',
    icon: 'mastodon',
    link: 'https://mastodon.social/@lissy93',
    color: '#6364FF',
  },
  {
    title: 'Dev',
    icon: 'dev',
    link: 'https://dev.to/lissy93',
    color: '#cece04',
  },
  {
    title: 'LinkedIn',
    icon: 'linkedin',
    link: 'https://linkedin.com/in/aliciasykes',
    color: '#0A66C2',
  },
];

export const aboutOurData = `
All data is stored in 
[\`awesome-privacy.yml\`](https://github.com/lissy93/awesome-privacy/blob/main/awesome-privacy.yml).

This file is then pulled into the website at build-time, and also used to generate
the repositories README file.
We use this method in the interest of transparency and data integrity,
as Git makes it possible to maintain a full log of what was changed, when, by who and why.

### Augmention
The data is augmented with some extra info, to add additional context to each service.
The aim of this is to give you a broader picture of each listing, to help you make a more informed decision.
Currently, this extra data is pulled from:

- **Privacy Policy** - To fetch a summerized version of each services Privacy Policy
	- Including policy and terms of service links, postives + negatives and privacy score
	- <small>Via [ToS;DR](https://tosdr.org/)</small>
- **GitHub** - To fetch info about each project's source code
	- Including author & contributors, creation & last updated date, languages, license and star count
	- <small>Via the [GitHub API](https://developer.github.com/v3/)</small>
- **Android App** - To fetch privacy info about each project's Android app
	- Including permissions, trackers, privacy score and metdata
	- <small>Via [Exodus Privacy](https://exodus-privacy.eu.org/)</small>
- **iOS App** - To fetch info about each project's iOS app
	- Including app size, rating, publish/update date, author and screenshots
	- <small>Via [Apple App Store](https://developer.apple.com/documentation/appstoreconnectapi/app_store)</small>
- **Docker** - To fetch info about each project's Docker image (if it's self-hosted)
	- Including supported architectures, run command, pull count, last updated and config options
	- <small>Via [Portainer-Templates](https://portainer-templates.as93.net/) and the [Docker Hub](https://hub.docker.com/) API</small>
- **Website** - To fetch privacy info about each project's website
	- Including SSL chain, WHOIS, server location, blacklist check and a screenshot
	- <small>Via [Web-Check](https://web-check.xyz/)</small>
- **Socials** - To fetch info about each project's social media presence
	- Including follower count, post frequency, engagement and a screenshot
	- <small>Via the Reddit, Discord and Twitter APIs</small>
- **User Reviews** - User-submitted comments + feedback on a given service
	- <small>Implemented using self-hosted instance of Remark42</small>

### API
We also have a free, no-auth, CORS-enabled RESR API,
which you can use to access Awesome Privacy's data programmatically,
or to build your own apps on top of it.

The [Swagger Spec](api) outlines all endpoints, usage and examples.

Use our public instance, at: \`https://api.awesome-privacy.xyz\` or [self-host your own](https://github.com/Lissy93/awesome-privacy/tree/main/api)
`;

export const projectRequirements = `
For software to be included in this list, it must meet the following requirements: 

- **Privacy Respecting**
	- The project must respect users privacy, not collect more data than necessary, and store info securely
	- For hosted services, the project must have a clear privacy policy
	- The user must remain in full control of their data, and be able to delete it at any time
- **Secure**
  - The software must be secure by default, without requiring additional configuration
  - There should be no current, critical security issues
  - The handling of past issues must have been prompt, transparent and effective
  - Ideally hosted services should have been security audited, with the report published publicly
- **Open Source**
	- The full source code should be released under an open source license
	- Ideally it should be possible for the user to build and run/deploy the software themselves from source
- **Actively Maintained**
  - The developers should address dependency updates and security patches in a timely manner
  - Ideally the source should have been updated within the last 12 months 
- **Transparent**
  - It should be clear who is behind the project, what their motives are, and what (if any) the funding model is
  - For hosted solutions, the privacy policy should clearly state what data is collected, how it's used and how long it's stored
- **Ethical**
  - Must not suppress free speech, discriminate or disregard any human rights
- **Relevant**
	- The software must be relevant, and fit into one of the existing categories
- **Functional**
	- Must be fully functional, and not just a concept or idea
	- A stable (non-alpha/beta) release is required at a minimum
	- Must be accessible to the general public, and not just a select group of people
	- If technical knowledge is required to run it, the software must be well documented

_There may be some exceptions, but these would need to be fully justified, reviewed
by the community, and the drawbacks / anti-features must be clearly listed along-side the software.
Usually these entries go within the "Notable Mentions" section instead._
`;

export const appDescription =
  'Privacy is a fundamental human right; ' +
  "without it, we're just open books in a world where everyone's " +
  "watching. Let's take control back.\n" +
  'Migrating open-source applications which do not collect, sell or log your data is a great first step.' +
  'Awesome Privacy is a directory of alternative privacy-respecting software and services.';

export default {
  title: 'Awesome Privacy | The Ultimate List of Private Apps',
  description:
    'Your guide to finding privacy-respecting alternatives to popular software and services.',
  keywords:
    'security, privacy, awesome privacy, data collection, free software, open source, privacy tools, privacy respecting software',
  author: 'Alicia Sykes',
  authorProjects,
  authorSocials,
  aboutOurData,
  projectRequirements,
  appDescription,
};
