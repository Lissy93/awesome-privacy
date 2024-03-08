
export interface ShortService {
  name: string;
  description: string;
  url: string;
}

export interface Service extends ShortService {
  github?: string;
  icon?: string;
  followWith?: string;
  securityAudited?: boolean;
  openSource?: boolean;
  acceptsCrypto?: boolean;
  tosdrId?: number;
}

export interface Section {
  name: string;
  services: Service[];
  intro?: string;
  notableMentions?: ShortService[] | string;
  furtherInfo?: string;
  wordOfWarning?: string;
  alternativeTo?: string[];
}

export interface Category {
  name: string;
  sections: Section[];
}

export interface AwesomePrivacy {
  categories: Category[];
}
