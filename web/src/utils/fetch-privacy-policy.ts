
export const fetchTosdrPrivacy = async (serviceId: string): Promise<PrivacyPolicyResponse | null> => {
  const endpoint = `https://api.tosdr.org/service/v2?id=${serviceId}`;
  try {
    return await fetch(endpoint).then((res) => res.json());
  } catch (error) {
    console.error('Error fetching privacy policy data:', error);
    return null;
  }
};

interface Document {
  id: number;
  name: string;
  url: string;
  updated_at: string;
  created_at: string;
}

interface Case {
  id: number;
  weight: number;
  title: string;
  description: string;
  updated_at: string;
  created_at: string;
  topic_id: number;
  classification: string;
}

interface Point {
  id: number;
  title: string;
  source: string;
  status: string;
  analysis: string;
  case: Case;
  document_id: number | null;
  updated_at: string;
  created_at: string;
}

interface Params {
  id: number;
  is_comprehensively_reviewed: boolean;
  name: string;
  updated_at: string;
  created_at: string;
  slug: string;
  rating: string;
  urls: string[];
  image: string;
  documents: Document[];
  points: Point[];
}

export interface PrivacyPolicyResponse {
  error: number;
  message: string;
  parameters: Params;
}
