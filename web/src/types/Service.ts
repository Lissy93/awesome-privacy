

export interface ShortService {
  name: string;
  description: string;
  url: string;
}

export interface Service {
  name: string;
  description: string;
  url: string;
  github: string;
  followWith?: string;
}

export interface Section {
  name: string;
  services: Service[];
  notableMentions: ShortService[];
  furtherInfo: string;
}

export interface ServiceStats {
  isOpenSource: boolean;
  author: string;
  authorUrl: string;
}

export interface AwesomePrivacy {
  categories: Array<{
    name: string;
    sections: Array<Section>;
  }>;
}
