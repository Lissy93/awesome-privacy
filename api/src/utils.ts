import * as yaml from 'js-yaml';

import type { AwesomePrivacy, Service } from './types';

/* Given a category/section/listing title, return it's slug/ID */
export const slugify = (title: string): string => title.toLowerCase().replace(/\s+/g, '-');

/* Base path, for fetching static files from GitHub CDN */
const ghCdnRoot = 'https://raw.githubusercontent.com/Lissy93/awesome-privacy';

/* Fetches and parses Awesome Privacy source data from GitHub CDN */
export const fetchAwesomePrivacyData = async (): Promise<AwesomePrivacy> => {
  const res = await fetch(`${ghCdnRoot}/main/awesome-privacy.yml`);
  const text = await res.text();
  return yaml.load(text) as AwesomePrivacy;
};

/* Returns all services as a flat array from Awesome Privacy */
export const fetchAllServices = async (): Promise<Service[]> => {
  const { categories } = await fetchAwesomePrivacyData();
  return categories.flatMap(category => category.sections.flatMap(section => section.services));
};

/* Find a given item by it's slug */
export const findBySlug = <T extends { name: string }>(collection: T[], slug: string): T | undefined =>
  collection.find(item => slugify(item.name) === slug);

/* For the homepage root, fetch and render the Swagger docs */
export const renderRemoteIndex = async (ctx) => {
  const response = await fetch(`${ghCdnRoot}/main/api/public/index.html`);
  if (response.ok) {
    const htmlContent = await response.text();
    return ctx.html(htmlContent);
  } else {
    return ctx.text('Unable to fetch the page', 502);
  }
};
