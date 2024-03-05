import type { APIRoute } from 'astro';
import yaml from 'js-yaml';

import type { AwesomePrivacy } from '../../types/Service';

const awesomePrivacyYamlPath = 'https://raw.githubusercontent.com/Lissy93/awesome-privacy/main/awesome-privacy.yml';

export const GET: APIRoute = async () => {

  const yamlContent = await fetch(awesomePrivacyYamlPath)
  .then(response => response.text())
  .catch(error => {
    return JSON.stringify({ error: "Failed to fetch YAML file", details: error });
  });

  const yamlObject = yaml.load(yamlContent) as AwesomePrivacy;

  return new Response(
    JSON.stringify(yamlObject), { headers: { 'content-type': 'application/json' } }
  )
}
