import { defineConfig } from 'astro/config';
import svelte from '@astrojs/svelte';
import partytown from '@astrojs/partytown';
import sitemap from '@astrojs/sitemap';
import vercel from "@astrojs/vercel/serverless";
// import netlify from "@astrojs/netlify";

const siteMapConfig = {
  entryLimit: 10000,
  changefreq: 'weekly',
  priority: 0.7,
  lastmod: new Date(),
  filter: (page) => { // Exclude search result pages
    return !page.url.startsWith('/search/') && page.url.split('/').length > 2;
  },
};

export default defineConfig({
  output: 'hybrid',
  integrations: [svelte(), partytown(), sitemap(siteMapConfig)],
  site: import.meta.env.SITE_URL || 'https://awesome-privacy.xyz',
  adapter: vercel(),
  // adapter: netlify(),
});
