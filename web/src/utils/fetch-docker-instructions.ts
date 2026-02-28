import { error } from './logger';

export const fetchDockerData = async (
  serviceName: string,
): Promise<TemplateResponse | null> => {
  const endpoint = `https://docker-info.as93.workers.dev/${serviceName}`;
  try {
    const res = await fetch(endpoint);
    if (!res.ok) {
      error('Docker', `HTTP ${res.status} for ${serviceName} (${endpoint})`);
      return null;
    }
    return await res.json();
  } catch (err) {
    error('Docker', `Network error for ${serviceName}: ${err}`);
    return null;
  }
};

interface DockerTemplatePort {
  privatePort: number;
  publicPort: number;
  type: string; // Typically TCP/UDP
}

interface DockerTemplateEnvironmentVariable {
  name: string;
  label?: string;
  default?: string;
  description?: string;
}

interface DockerTemplateVolume {
  bind: string;
  container: string;
  readonly?: boolean;
}

interface DockerTemplate {
  name?: string;
  title: string;
  description?: string;
  logo?: string;
  image: string;
  categories?: string[];
  ports?: DockerTemplatePort[];
  env?: DockerTemplateEnvironmentVariable[];
  volumes?: DockerTemplateVolume[];
  restart_policy?: string; // Typically "no", "always", "unless-stopped", "on-failure"
}

interface DockerHubData {
  user: string;
  name: string;
  namespace: string;
  repository_type: string;
  status: number;
  description: string;
  is_private: boolean;
  is_automated: boolean;
  can_edit: boolean;
  star_count: number;
  pull_count: number;
  last_updated: string;
  date_registered: string;
  build_status: string;
  permissions: {
    read: boolean;
    write: boolean;
    admin: boolean;
  };
}

interface DockerUsage {
  dockerRunCommand: string;
  dockerComposeFile: string;
}

export interface TemplateResponse {
  found: boolean;
  error: string | null;
  template?: DockerTemplate;
  dockerHubData?: DockerHubData;
  usage?: DockerUsage;
}
