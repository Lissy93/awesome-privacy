import type { Category } from '../types/Service';

export const prepareSearchItems = (categories: Category[]) => {
  const items: any = [];
  // Add each category
  categories.forEach((category) => {
    items.push({
      type: 'Category',
      category: category.name,
      itemCount: (category.sections || []).reduce((acc, section) => {
        return acc + (section.services || []).length;
      }, 0),
    });

    // Add section with category context
    category.sections.forEach((section) => {
      items.push({
        type: 'Section',
        sectionName: section.name,
        description: section.intro || '',
        category: category.name,
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
          category: category.name,
          sectionName: section.name,
          logo: service.icon || '',
        });
      });
    });
  });
  return items;
};

export const searchOptions = {
  includeScore: true,
  keys: [
    { name: 'name', weight: 0.9 },
    { name: 'sectionName', weight: 0.8 },
    { name: 'category', weight: 0.7 },
    { name: 'notableMentions', weight: 0.5 },
    { name: 'alternativeTo', weight: 0.5 },
    { name: 'github', weight: 0.4 },
    { name: 'url', weight: 0.2 },
    { name: 'description', weight: 0.1 },
    { name: 'intro', weight: 0.1 },
    { name: 'furtherInfo', weight: 0.1 },
    { name: 'wordOfWarning', weight: 0.1 },
  ],
};
