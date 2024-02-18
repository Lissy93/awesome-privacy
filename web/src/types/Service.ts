

export interface ShortService {
  name: string;
  description: string;
  url: string;
}

export interface Service {
  name: string;
  description: string;
  url: string;
  github?: string;
  icon?: string;
  followWith?: string;
  securityAudited?: boolean;
  openSource?: boolean;
  acceptsCrypto?: boolean;
}

export interface Section {
  name: string;
  services: Service[];
  intro?: string;
  notableMentions?: ShortService[] | string;
  furtherInfo?: string;
  wordOfWarning?: string;
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
