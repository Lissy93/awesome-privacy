export const fetchWebsiteInfo = async (
  url: string,
): Promise<WebsiteData | null> => {
  const endpoint = `https://site-info-fetch.as93.workers.dev/?url=${url}`;
  try {
    return await fetch(endpoint).then((res) => res.json());
  } catch (error) {
    console.error('Error fetching website info:', error);
    return null;
  }
};

interface DNSRecord {
  target: string;
  ip: string;
  country_code: string;
  country_name: string;
  isp: string;
}

interface DNSRecords {
  ns: {
    records: DNSRecord[];
  };
  mx: {
    records: DNSRecord[];
  };
}

interface Engine {
  name: string;
  reference: string;
  detected: boolean;
}

interface DomainBlacklist {
  engines: Engine[];
  detections: number;
}

interface FileType {
  signature: string;
  extension: string;
  headers: string;
}

interface GeoLocation {
  countries: string[];
}

interface HtmlForms {
  number_of_total_forms: number;
  number_of_total_input_fields: number;
  two_text_inputs_in_a_form: boolean;
  credit_card_field_present: boolean;
  password_field_present: boolean;
  email_field_present: boolean;
}

interface Redirection {
  found: boolean;
  external: boolean;
  url: string;
  redirects: string[];
}

interface ResponseHeaders {
  code: number;
  status: string;
  date: string;
  last_modified: string;
  etag: string;
  accept_ranges: string;
  vary: string;
  content_encoding: string;
  cache_control: string;
  content_length: string;
  content_type: string;
  age: string;
  content_security_policy_report_only: string;
  strict_transport_security: string;
  public_key_pins_report_only: string;
  x_frame_options: string;
  x_content_type_options: string;
  x_xss_protection: string;
  referrer_policy: string;
  x_permitted_cross_domain_policies: string;
  onion_location: string;
}

interface RiskScore {
  result: number;
}

interface SecurityChecks {
  [key: string]: boolean | string;
}

interface ServerDetails {
  ip: string;
  hostname: string;
  continent_code: string;
  continent_name: string;
  country_code: string;
  country_name: string;
  region_name: string;
  city_name: string;
  latitude: number;
  longitude: number;
  isp: string;
  asn: string;
}

interface SiteCategory {
  [key: string]: boolean;
}

interface UrlParts {
  scheme: string;
  host: string;
  host_nowww: string;
  port: null | number;
  path: null | string;
  query: null | string;
}

interface WebPage {
  title: string;
  description: string;
  keywords: string;
}

export interface WebsiteData {
  dns_records: DNSRecords;
  domain_blacklist: DomainBlacklist;
  file_type: FileType;
  geo_location: GeoLocation;
  html_forms: HtmlForms;
  redirection: Redirection;
  response_headers: ResponseHeaders;
  risk_score: RiskScore;
  security_checks: SecurityChecks;
  server_details: ServerDetails;
  site_category: SiteCategory;
  url_parts: UrlParts;
  web_page: WebPage;
}
