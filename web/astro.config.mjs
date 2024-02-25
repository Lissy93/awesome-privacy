import { defineConfig } from 'astro/config';
import svelte from '@astrojs/svelte';
import partytown from '@astrojs/partytown';
import sitemap from '@astrojs/sitemap';
import vercel from "@astrojs/vercel/serverless";
// import netlify from "@astrojs/netlify";

export default defineConfig({
  output: 'hybrid',
  integrations: [svelte(), partytown(), sitemap()],
  site: import.meta.env.SITE_URL || 'https://awesome-privacy.xyz',
  adapter: vercel(),
  // adapter: netlify(),
});
