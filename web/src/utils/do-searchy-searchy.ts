import Fuse from 'fuse.js';

import type { Category, Service } from '../types/Service';
import { fetchCategories, slugify } from './fetch-data';

export interface SearchItem {
  type: 'Category' | 'Section' | 'Service';
  category: string;
  path: string;
  itemCount?: number;
  sectionName?: string;
  description?: string;
  name?: string;
  url?: string;
  github?: string;
  codeberg?: string;
  git?: string;
  logo?: string;
  platforms?: string[];
  traits?: string[];
  alternativeTo?: string[];
  service?: Service;
}

export const prepareSearchItems = (categories: Category[]): SearchItem[] => {
  const items: SearchItem[] = [];
  // Add each category
  categories.forEach((category) => {
    const categoryPath = `/${slugify(category.name)}/`;
    items.push({
      type: 'Category',
      category: category.name,
      path: categoryPath,
      itemCount: (category.sections || []).reduce((acc, section) => {
        return acc + (section.services || []).length;
      }, 0),
    });

    // Add section with category context
    (category.sections || []).forEach((section) => {
      const sectionPath = `${categoryPath}${slugify(section.name)}/`;
      items.push({
        type: 'Section',
        sectionName: section.name,
        description: section.intro || '',
        category: category.name,
        path: sectionPath,
        itemCount: (section.services || []).length,
      });

      // Add service with section and category context
      (section.services || []).forEach((service) => {
        items.push({
          type: 'Service',
          name: service.name,
          description: service.description,
          url: service.url,
          github: service.github || '',
          codeberg: service.codeberg || '',
          git: service.git || '',
          category: category.name,
          sectionName: section.name,
          path: `${sectionPath}${slugify(service.name)}/`,
          logo: service.icon || '',
          // Get the platform from followWith field or android/ios app
          platforms: Object.keys(service)
            .filter((key) => key.endsWith('App'))
            .map((key) => key.replace(/App$/, ''))
            .concat(service.followWith || []),
          // Boolean fields, as words: `openSource` -> "open source"
          traits: Object.entries(service)
            .filter(([, value]) => value === true)
            .map(([key]) =>
              key.replace(/[A-Z]/g, (c) => ` ${c.toLowerCase()}`),
            ),
          // The proprietary tools this section replaces, eg "whatsapp"
          alternativeTo: section.alternativeTo || [],
          // Kept so results can render a card without a second lookup
          service,
        });
      });
    });
  });
  return items;
};

// Set the fuzziness power. 0 = perfect match, and 1 = barely matched
export const SEARCH_SCORE_CUTOFF = 0.85;

export const isRelevant = (result: { score?: number }): boolean =>
  (result.score ?? 0) <= SEARCH_SCORE_CUTOFF;

export const searchOptions = {
  includeScore: true,
  ignoreLocation: true,
  threshold: 0.3,
  keys: [
    { name: 'name', weight: 0.9 },
    { name: 'sectionName', weight: 0.8 },
    { name: 'alternativeTo', weight: 0.8 },
    { name: 'category', weight: 0.7 },
    { name: 'platforms', weight: 0.6 },
    { name: 'traits', weight: 0.6 },
    { name: 'github', weight: 0.4 },
    { name: 'codeberg', weight: 0.4 },
    { name: 'git', weight: 0.3 },
    { name: 'url', weight: 0.2 },
    { name: 'description', weight: 0.1 },
  ],
};

// Built once per page, and shared by the search box and the results island
let indexPromise: Promise<Fuse<SearchItem>> | null = null;

export const getSearchIndex = (): Promise<Fuse<SearchItem>> =>
  (indexPromise ??= fetchCategories().then((categories) => {
    // Caching a failed fetch would leave search empty for the whole session
    if (!categories.length) indexPromise = null;
    return new Fuse(prepareSearchItems(categories), searchOptions);
  }));

export const runSearch = async (term: string): Promise<SearchItem[]> =>
  term
    ? (await getSearchIndex())
        .search(term)
        .filter(isRelevant)
        .map((r) => r.item)
    : [];
