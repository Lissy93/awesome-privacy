
import yaml from 'js-yaml';

import type { AwesomePrivacy } from '../types/Service';

export const fetchData = async (): Promise<AwesomePrivacy> => {
  return await fetch('http://localhost:4321/awesome-privacy.yml')
    .then((res) => res.text())
    .then((data) => yaml.load(data))
    .catch((err) => console.error('ah crap', err)) as AwesomePrivacy;
}

export const slugify = (title: string) => {
  return title.toLowerCase().replace(/\s/g, '-');
};
