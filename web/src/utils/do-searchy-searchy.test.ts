import { describe, it, expect } from 'vitest';
import { prepareSearchItems } from './do-searchy-searchy';
import type { Category } from '../types/Service';

const makeCategory = (overrides: Partial<Category> = {}): Category =>
  ({
    name: 'Test Category',
    sections: [],
    ...overrides,
  }) as Category;

describe('prepareSearchItems', () => {
  it('returns an empty array for no categories', () => {
    expect(prepareSearchItems([])).toEqual([]);
  });

  it('creates a category item', () => {
    const categories = [makeCategory({ name: 'Privacy Tools' })];
    const items = prepareSearchItems(categories);
    expect(items).toHaveLength(1);
    expect(items[0]).toMatchObject({
      type: 'Category',
      category: 'Privacy Tools',
      itemCount: 0,
    });
  });

  it('creates section items with category context', () => {
    const categories = [
      makeCategory({
        name: 'Comms',
        sections: [
          { name: 'Messaging', intro: 'Secure messaging apps', services: [] },
        ],
      }),
    ] as Category[];
    const items = prepareSearchItems(categories);
    const section = items.find((i: { type: string }) => i.type === 'Section');
    expect(section).toMatchObject({
      type: 'Section',
      sectionName: 'Messaging',
      description: 'Secure messaging apps',
      category: 'Comms',
      itemCount: 0,
    });
  });

  it('creates service items with section and category context', () => {
    const categories = [
      makeCategory({
        name: 'Comms',
        sections: [
          {
            name: 'Messaging',
            services: [
              {
                name: 'Signal',
                description: 'Encrypted messenger',
                url: 'https://signal.org',
                github: 'signalapp/Signal-Android',
                icon: 'signal.png',
              },
            ],
          },
        ],
      }),
    ] as Category[];
    const items = prepareSearchItems(categories);
    const service = items.find((i: { type: string }) => i.type === 'Service');
    expect(service).toMatchObject({
      type: 'Service',
      name: 'Signal',
      description: 'Encrypted messenger',
      url: 'https://signal.org',
      github: 'signalapp/Signal-Android',
      category: 'Comms',
      sectionName: 'Messaging',
      logo: 'signal.png',
    });
  });

  it('counts services across sections for category itemCount', () => {
    const categories = [
      makeCategory({
        name: 'Tools',
        sections: [
          {
            name: 'A',
            services: [
              { name: 's1', description: '', url: '' },
              { name: 's2', description: '', url: '' },
            ],
          },
          {
            name: 'B',
            services: [{ name: 's3', description: '', url: '' }],
          },
        ],
      }),
    ] as Category[];
    const items = prepareSearchItems(categories);
    const cat = items.find((i: { type: string }) => i.type === 'Category');
    expect(cat.itemCount).toBe(3);
  });
});
