
WEBSITE SOURCE CODE
-------------------
This is the source code for the awesome-privacy website, which is deployed at
https://awesome-privacy.xyz.

================================================================================

DEVELOPMENT SETUP
-----------------
To get started, you'll need Node and Git installed.
Then run the following commands:

# 1. Clone the repo
git clone git@github.com:Lissy93/awesome-privacy.git
# 2. Navigate into it
cd awesome-privacy/web
# 3. Install dependencies
yarn install
# 4. Start the development server
yarn dev
5. Open browser
open http://127.0.0.1:4321

================================================================================

DEPLOYMENT
----------
You have several options for deploying your own instance of Awesome Privacy
Option 1) Run `yarn build`, and copy the contents of `dist` to any web server/ CDN
Option 2) Fork the repo and import it to a provider of your choice (Netlify or Vercel)
Option 3) Use the included Dockerfile to build and run the application on any server

================================================================================

TECHNOLOGY
----------
The website is built with Astro, and statically generated at build-time.
This means that changes to the data will not be reflected until the site is rebuilt.
Dynamic elems (search + comments) are built as Svelte islands, and rehydrated at runtime.
Most the code is written in Typescript. We're not using a CSS library, just plain SASS.

The site also uses:
- Fuse.js for fuzzy search
- js-yaml for parsing YAML
- marked for markdown rendering
- fontawesome for iconography

================================================================================

DATA
----
All data relating to software/apps/services used on the website is pulled from:
https://github.com/Lissy93/awesome-privacy/blob/main/awesome-privacy.yml (CC0-1.0)
If you only wish to update content, there's no need to edit the site's source code

================================================================================

SITE STRUCTURE
--------------
All views are located in /src/pages.
The general site structure is as follows:

/
├── about
├── search
│   └── [query]
├── browse
└── [category-name]
    └── [section]
        └── [service]

Assets in /public will be served from the top-level (favicon, pwa assets, sitemap)

================================================================================

THIRD-PARTY SERVICES
--------------------

Infra:
- Vercel - This is where the site is hosted
- GitHub - This is where the source code is stored
- Cloudflare - This is where the domain is managed

Monitoring:
- Plausible (self-hosted) - For basic hit counting and traffic stats
  (this does NOT collect nor store IP, user agent or any other personal info)
- GlitchTip (self-hosted) - For error tracking and reporting
- UptimeKuma (self-hosted) - For down detection and basic monitoring

External Requests:
- Service icons are pulled from the respective service's website
- Comments are handled by Remark42 (self-hosted)
- Fonts which can not be loaded from /public will fallback to Google Fonts CDN
- Service icons which are not found, will be replaced from icon.horse
- Open source stats on services are fetched from the GitHub API

================================================================================

LICENSE
-------
The data (in /awesome-privacy.yml) is licensed under Creative Commons CC0-1.0 
The website source code, and all other content is licensed under the MIT License

(C) Alicia Sykes <https://aliciasykes.com> 2024

Permission is hereby granted, free of charge, to any person obtaining a copy 
of this software and associated documentation files (the "Software"), to deal 
in the Software without restriction, including without limitation the rights 
to use, copy, modify, merge, publish, distribute, sub-license, and/or sell 
copies of the Software, and to permit persons to whom the Software is furnished 
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included install 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANT ABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL 
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

================================================================================



