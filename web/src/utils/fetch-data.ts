import yaml from 'js-yaml';

import type { AwesomePrivacy } from '../types/Service';

const awesomePrivacyData =
  'https://raw.githubusercontent.com/Lissy93/awesome-privacy/main/awesome-privacy.yml';

export const fetchData = async (): Promise<AwesomePrivacy> => {
  return (await fetch(awesomePrivacyData)
    .then((res) => res.text())
    .then((data) => yaml.load(data))
    .catch((err) => console.error('ah crap', err))) as AwesomePrivacy;
};

export const slugify = (title: string) => {
  return (title || '')
    .toLowerCase()
    .replace(/\s/g, '-')
    .replace(/\+|&/g, 'and')
    .replaceAll('?', '');
};
