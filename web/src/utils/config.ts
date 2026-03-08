function cleanUrl(inputString: string) {
  return inputString.replace(/['";]+/g, '').trim();
}

export const site = cleanUrl(
  import.meta.env.SITE_URL || 'https://awesome-privacy.xyz',
);

export const title =
  'Awesome Privacy | Compare privacy-respecting alternatives to popular software & services';

export const description =
  'Your guide to escaping big tech, protecting your privacy, and reclaiming your digital life.';
