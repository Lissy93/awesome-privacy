import yaml from 'js-yaml';
import { error } from './logger';

import type { AwesomePrivacy } from '../types/Service';

const awesomePrivacyData =
  'https://raw.githubusercontent.com/Lissy93/awesome-privacy/main/awesome-privacy.yml';

export const fetchData = async (): Promise<AwesomePrivacy> => {
  try {
    const res = await fetch(awesomePrivacyData);
    if (!res.ok) {
      error('Data', `HTTP ${res.status} fetching awesome-privacy.yml (${awesomePrivacyData})`);
      return {} as AwesomePrivacy;
    }
    const text = await res.text();
    return yaml.load(text) as AwesomePrivacy;
  } catch (err) {
    error('Data', `Failed to fetch awesome-privacy.yml: ${err}`);
    return {} as AwesomePrivacy;
  }
};

export const slugify = (title: string) => {
  return (title || '')
    .toLowerCase()
    .replace(/\s/g, '-')
    .replace(/\+|&/g, 'and')
    .replaceAll('?', '');
};
