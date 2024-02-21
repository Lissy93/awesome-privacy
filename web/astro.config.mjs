import { defineConfig } from 'astro/config';

import svelte from '@astrojs/svelte';
import partytown from '@astrojs/partytown';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  integrations: [
    svelte(),
    partytown(),
    sitemap(),
  ],
  site: import.meta.env.SITE_URL || 'https://awesome-privacy.xyz',
});
