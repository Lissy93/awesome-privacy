import { Hono } from 'hono';
import { cors } from 'hono/cors';
import Fuse from 'fuse.js';

import {
  fetchAllServices,
  fetchAwesomePrivacyData,
  findBySlug,
  slugify,
  renderRemoteIndex,
} from './utils';

import index from '../public/index.html'

/* Create new Hono app */
const app = new Hono({ strict: false });

/* Enable CORS for all routes */
app.use('*', cors());

/* Serve the index page (which contains the Swagger Docs) */
app.get("/", async (ctx) => {
  if (index) {
    return ctx.html(index)
  } else {
    return renderRemoteIndex(ctx);
  }
});

/* Returns an array all service objects */
app.get('/services', async (c) => {
  return c.json(await fetchAllServices());
});

/* Returns an array of all categories IDs */
app.get('/categories', async (c) => {
  const { categories } = await fetchAwesomePrivacyData();
  return c.json(categories.map(({ name }) => slugify(name)));
});

app.get('/search', async (c) => {
  return c.json({ error: 'Search term not specified' }, 404)
});

/* Search results, returns an array of listing which match a given search term  */
app.get('/search/:searchTerm', async (c) => {
  const services = await fetchAllServices();
  const options = {
    includeScore: true,
    keys: ['name', 'description', 'followWith']
  };
  const fuse = new Fuse(services, options);
  const searchTerm = c.req.param('searchTerm');
  const result = fuse.search(searchTerm);
  const mappedResults = result.map(({ item, score }) => ({ ...item, score }));
  return c.json(mappedResults);
});

/* Returns an array of all section IDs within a given category */
app.get('/:category', async (c) => {
  const { categories } = await fetchAwesomePrivacyData();
  const category = findBySlug(categories, c.req.param('category'));
  return category ? c.json(category.sections.map(({ name }) => slugify(name)))
    : c.json({ error: 'Category not found' }, 404);
});

/* Returns an array of all service objects within a given section */
app.get('/:category/:section', async (c) => {
  const { categories } = await fetchAwesomePrivacyData();
  const category = findBySlug(categories, c.req.param('category'));
  const section = findBySlug(category?.sections || [], c.req.param('section'));
  return section ? c.json(section.services || []) : c.json({ error: 'Section not found' }, 404);
});

/* Returns a single service object, for a given category, section and service */
app.get('/:category/:section/:service', async (c) => {
  const { categories } = await fetchAwesomePrivacyData();
  const category = findBySlug(categories, c.req.param('category'));
  const section = findBySlug(category?.sections || [], c.req.param('section'));
  const service = findBySlug(section?.services || [], c.req.param('service'));
  return service ? c.json(service) : c.json({ error: 'Service not found' }, 404);
});

export default app;
