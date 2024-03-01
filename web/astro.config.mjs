import { defineConfig } from 'astro/config';

// Integrations
import svelte from '@astrojs/svelte';
import partytown from '@astrojs/partytown';
import sitemap from '@astrojs/sitemap';

// Adapters
import vercelAdapter from '@astrojs/vercel/serverless';
import netlifyAdapter from '@astrojs/netlify';
import nodeAdapter from '@astrojs/node';
import cloudflareAdapter from '@astrojs/cloudflare';

// Determine the deploy target (vercel, netlify, cloudflare, node)
const deployTarget = import.meta.env.DEPLOY_TARGET || 'vercel';

// Determine the output mode (server or hybrid)
const output = import.meta.env.OUTPUT || 'hybrid';

// The FQDN of where the site is hosted (used for sitemaps & canonical URLs)
const site = import.meta.env.SITE_URL || 'https://awesome-privacy.xyz';

// Initialize Astro integrations
const integrations = [svelte(), partytown(), sitemap()];

// Set the appropriate adapter, based on the deploy target
const adapter = {
  vercel: vercelAdapter(),
  netlify: netlifyAdapter(),
  cloudflare: cloudflareAdapter(),
  node: nodeAdapter({
    mode: 'standalone',
  }),
}[deployTarget];

// Export Astro configuration
export default defineConfig({ output, integrations, site, adapter });
