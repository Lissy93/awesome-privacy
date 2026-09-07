import type { APIRoute } from 'astro';
import * as yaml from 'js-yaml';

import type { AwesomePrivacy } from '../../types/Service';

const awesomePrivacyYamlPath =
  'https://raw.githubusercontent.com/Lissy93/awesome-privacy/main/awesome-privacy.yml';

export const GET: APIRoute = async () => {
  const response = await fetch(awesomePrivacyYamlPath).catch(() => null);
  const data = response?.ok
    ? (yaml.load(await response.text()) as AwesomePrivacy)
    : null;

  // Caching a failed fetch would serve a broken dataset for the whole max-age
  if (!data?.categories) {
    return new Response(JSON.stringify({ error: 'Failed to fetch dataset' }), {
      status: 502,
      headers: {
        'content-type': 'application/json',
        'cache-control': 'no-store',
      },
    });
  }

  return new Response(JSON.stringify(data), {
    headers: {
      'content-type': 'application/json',
      // ~250KB fetched from GitHub raw, and it only changes on merge
      'cache-control': 'public, max-age=300, stale-while-revalidate=86400',
    },
  });
};
