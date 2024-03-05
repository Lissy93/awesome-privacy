import type { APIRoute } from 'astro';
import yaml from 'js-yaml';

import type { AwesomePrivacy, Service } from '../../types/Service';

interface LineNumberRange {
  start: number;
  end: number;
}

interface LineNumberData {
  [category: string]: {
    [section: string]: {
      [service: string]: {
        lineNumbers: LineNumberRange | null;
        yaml: string;
      }
    };
  };
}

const awesomePrivacyYamlPath = 'https://raw.githubusercontent.com/Lissy93/awesome-privacy/main/awesome-privacy.yml';

/**
 * Given a service object and an array of string lines from the raw YAML
 * Find the starting and ending line number for that service
 */
const calculateServiceRange = (service: Service, yamlLines: string[]): LineNumberRange | null => {
  const lookFor = `- name: ${service.name}`;
  const start = yamlLines.findIndex(line => line.includes(lookFor)) + 1;
  if (start === -1) return null;
  const detectEnd = (line: string) => {
    return line.trim().length === 0
    || line.startsWith('  - ')
    || line.includes('notableMentions:')
    || line.includes('furtherInfo:')
    || line.includes('wordOfWarning:')
  }
  const remainingLines = yamlLines.slice(start);
  const end = start + remainingLines.findIndex(detectEnd);
  
  return { start, end };
}

/**
 * Given a service object, convert it into a correctly formatted YAML string
 */
const convertJsonIntoYaml = (service: Service): string => {
  return yaml.dump(service);
};

/**
 * Given the object representation of the YAML and the array of lines from the raw YAML
 * Organize the data into a format that can be returned as JSON
 */
const makeResults = (yamlObject: AwesomePrivacy, yamlLines: string[]): LineNumberData => {
  const organizedData: LineNumberData = {};
  yamlObject.categories.forEach((category) => {
    organizedData[category.name] = {};
    category.sections.forEach((section) => {
      organizedData[category.name][section.name] = {};
      section.services.forEach((service) => {
        organizedData[category.name][section.name][service.name] = {
          lineNumbers: calculateServiceRange(service, yamlLines),
          yaml: convertJsonIntoYaml(service),
        };
      });
    });
  });
  return organizedData;
}

export const GET: APIRoute = async () => {

  // Fetch the raw YAML from the awesome-privacy repository
  const yamlContent = await fetch(awesomePrivacyYamlPath)
  .then(response => response.text())
  .catch(error => {
    return JSON.stringify({ error: "Failed to fetch YAML file", details: error });
  });

  // Array of lines from the raw YAML
  const yamlLines: string[] = yamlContent.split('\n');

  // Object representation of the YAML
  const yamlObject = yaml.load(yamlContent) as AwesomePrivacy;

  // Make results
  const results = makeResults(yamlObject, yamlLines);

  return new Response(
    JSON.stringify(results), { headers: { 'content-type': 'application/json' } }
  )
}
