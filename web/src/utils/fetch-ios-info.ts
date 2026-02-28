import { error } from './logger';

export const fetchIosInfo = async (
  iosUrl: string,
): Promise<IoSApiResponse | null> => {
  const endpoint = `https://ios-app-info.as93.net?appStoreUrl=${iosUrl}`;
  try {
    const res = await fetch(endpoint);
    if (!res.ok) {
      error('iOS', `HTTP ${res.status} for ${iosUrl} (${endpoint})`);
      return null;
    }
    return await res.json();
  } catch (err) {
    error('iOS', `Network error for ${iosUrl}: ${err}`);
    return null;
  }
};

export interface IoSApiResponse {
  artistViewUrl: string;
  releaseNotes: string;
  artworkUrl60: string;
  artworkUrl100: string;
  artworkUrl512: string;
  supportedDevices: string[];
  features: string[];
  screenshotUrls: string[];
  ipadScreenshotUrls: string[];
  appletvScreenshotUrls: string[];
  advisories: string[];
  isGameCenterEnabled: boolean;
  kind: string;
  fileSizeBytes: number;
  sellerUrl: string;
  formattedPrice: string;
  userRatingCountForCurrentVersion: number;
  trackContentRating: string;
  trackCensoredName: string;
  trackViewUrl: string;
  contentAdvisoryRating: string;
  artistId: number;
  artistName: string;
  genres: string[];
  price: number;
  trackId: number;
  trackName: string;
  description: string;
  currentVersionReleaseDate: string;
  averageUserRatingForCurrentVersion: number;
  isVppDeviceBasedLicensingEnabled: boolean;
  genreIds: string[];
  sellerName: string;
  languageCodesISO2A: string[];
  releaseDate: string;
  bundleId: string;
  currency: string;
  averageUserRating: number;
  minimumOsVersion: string;
  primaryGenreName: string;
  primaryGenreId: number;
  version: string;
  wrapperType: string;
  userRatingCount: number;
}
