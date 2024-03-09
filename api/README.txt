
AWESOME PRIVACY API SOURCE
============================================================================

ABOUT
-----
This directory contains the source for the Awesome Privacy API.
You can use the API to interact with our data programmatically.
The API is build using Hono, and intended for Cloudflare Workers.

============================================================================

PUBLIC INSTANCE
---------------
We have a free, no-auth, CORS-enabled instance which you can use.
Get started with the Swagger docs at https://api.awesomeprivacy.com

============================================================================

GETTING STARTED
---------------
1. You'll first need Git and Node.js installed on your system
2. Then install wrangler, `npm install wrangler --save-dev`
3. Download `git clone git@github.com:Lissy93/awesome-privacy.git`
4. And navigate int the api dir, with `cd awesome-privacy/api`
5. Install all required dependencies, by running `npm install`
4. Then run `yarn start` to start a local instance of the API

============================================================================

DEVELOPMENT
-----------
1. Run `yarn dev` to start a local instance of the API + Swagger interface
2. Open `http://localhost:9000` in your browser or with a HTTP client
3. Make any desired changes in `src/` - the server will automatically reload

============================================================================

DEPLOYMENT
----------
1. Sign up for Cloudflare Workers (https://workers.dev) - free tier is fine
2. Follow the steps in "Getting Started" to setup the project locally
3. Run `wrangler login` to login to your Cloudflare account in wrangler
4. Run `wrangler deploy` to publish the API to Cloudflare Workers

============================================================================

LICENSE
-------
This project is licensed under MIT, (C) Alicia Sykes <aliciasykes.com> 2024
See the GitHub repo for more info https://github.com/Lissy93/awesome-privacy

