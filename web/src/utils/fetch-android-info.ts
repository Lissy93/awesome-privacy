
const doubleCheckPackageName = (packageStr: string) => {
  return packageStr.includes('id=') ? packageStr.split('id=')[1] : packageStr;
}

export const fetchAndroidInfo = async (androidPackage: string): Promise<AndroidInfo | null> => {
  const endpoint = `https://android-app-privacy.as93.net/${doubleCheckPackageName(androidPackage)}`;
  try {
    return await fetch(endpoint).then((res) => res.json());
  } catch (error) {
    console.error('Error fetching android data:', error);
    return null;
  }
};

interface Tracker {
  id: number;
  name: string;
  description: string;
  creation_date: string;
  code_signature: string;
  network_signature: string;
  website: string;
  categories: string[];
  documentation: string[];
}

export interface AndroidInfo {
  error?: string;
  handle: string;
  app_name: string;
  uaid: string;
  version_name: string;
  version_code: string;
  source: string;
  icon_hash: string;
  apk_hash: string;
  created: string;
  updated: string;
  report: number;
  creator: string;
  downloads: string;
  trackers: Tracker[];
  permissions: string[];
}


