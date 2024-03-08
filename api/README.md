# Cloudflare Workers OpenAPI 3.1

This is a Cloudflare Worker with OpenAPI 3.1 using [itty-router-openapi](https://github.com/cloudflare/itty-router-openapi).

## Getting Started
1. You'll need Git and Node.js installed.
2. Then install [wrangler](https://developers.cloudflare.com/workers/cli-wrangler/install-update)
3. Clone this project, cd into it and install dependencies with `yarn install`
4. Run `yarn start` to start a local instance of the API.

## Development
1. Run `yarn dev` to start a local instance of the API.
2. Open `http://localhost:9000/` in your browser to see the Swagger interface where you can try the endpoints.
3. Changes made in the `src/` folder will automatically trigger the server to reload, you only need to refresh the Swagger interface.

## Deployment
1. Sign up for [Cloudflare Workers](https://workers.dev). The free tier is more than enough for most use cases.
2. Clone this project, cd into api and install dependencies with `yarn install`
3. Run `wrangler login` to login to your Cloudflare account in wrangler
4. Run `wrangler deploy` to publish the API to Cloudflare Workers
