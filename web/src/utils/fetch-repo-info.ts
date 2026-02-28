import { error } from './logger';

const githubHeaders = (): Record<string, string> => {
  const headers: Record<string, string> = {
    'User-Agent': 'awesome-privacy',
    'Accept': 'application/vnd.github.v3+json',
  };
  const token = import.meta.env.GITHUB_API_KEY;
  if (token) headers['Authorization'] = `token ${token}`;
  return headers;
};

const fetchFromGitHub = async (github: string): Promise<GitHubStatsResponse | null> => {
  const base = `https://api.github.com/repos/${github}`;
  const headers = githubHeaders();

  const [infoRes, langsRes, tagsRes, contribRes, commitsRes] = await Promise.all([
    fetch(base, { headers }),
    fetch(`${base}/languages`, { headers }),
    fetch(`${base}/tags`, { headers }),
    fetch(`${base}/contributors`, { headers }),
    fetch(`${base}/commits`, { headers }),
  ]);

  if (!infoRes.ok) {
    error('GitHub Stats', `GitHub API returned ${infoRes.status} for ${github}`);
    return null;
  }

  const parseJson = (r: Response) =>
    r.ok && r.status !== 204 ? r.json() : null;

  const [info, languages, tags, contributors, commits] = await Promise.all(
    [infoRes, langsRes, tagsRes, contribRes, commitsRes].map(parseJson),
  );

  return {
    info: {
      ownerUsername: info.owner?.login ?? '',
      ownerAvatar: info.owner?.avatar_url ?? '',
      description: info.description ?? '',
      url: info.html_url ?? '',
      homepage: info.homepage ?? '',
      language: info.language ?? '',
      topics: info.topics ?? [],
      license: info.license?.spdx_id ?? '',
      isFork: info.fork ?? false,
      isArchived: info.archived ?? false,
      createdAt: info.created_at ?? '',
      updatedAt: info.updated_at ?? '',
      size: info.size ?? 0,
      scarCount: info.stargazers_count ?? 0,
      forksCount: info.forks_count ?? 0,
      watchersCount: info.watchers_count ?? 0,
    },
    languages: languages ?? {},
    versions: (tags ?? []).map((tag: any) => ({
      name: tag.name,
      commit: tag.commit?.sha ?? '',
      zipball: tag.zipball_url ?? '',
      tarball: tag.tarball_url ?? '',
    })),
    contributors: (contributors ?? []).map((c: any) => ({
      username: c.login ?? '',
      avatar: c.avatar_url ?? '',
      contributions: c.contributions ?? 0,
    })),
    commits: (commits ?? []).map((c: any) => ({
      sha: c.sha ?? '',
      authorName: c.commit?.author?.name ?? '',
      authorDate: c.commit?.author?.date ?? '',
      message: c.commit?.message ?? '',
      authorUsername: c.author?.login ?? '',
      authorAvatar: c.author?.avatar_url ?? '',
    })),
  };
};

const fetchFromWorker = async (github: string): Promise<GitHubStatsResponse | null> => {
  const res = await fetch(`https://repo-info.as93.workers.dev/${github}`);
  if (!res.ok) return null;
  return res.json();
};

export const fetchGitHubStats = async (
  github: string,
): Promise<GitHubStatsResponse | null> => {
  try {
    const result = await fetchFromGitHub(github);
    if (result) return result;
    const fallback = await fetchFromWorker(github);
    if (fallback) return fallback;
    error('GitHub Stats', `Both direct API and worker failed for ${github}`);
    return null;
  } catch (err) {
    try {
      return await fetchFromWorker(github);
    } catch {
      error('GitHub Stats', `All fetches failed for ${github}: ${err}`);
      return null;
    }
  }
};

export interface GitHubStatsResponse {
  info: {
    ownerUsername: string;
    ownerAvatar: string;
    description: string;
    url: string;
    homepage: string;
    language: string;
    topics: string[];
    license: string;
    isFork: boolean;
    isArchived: boolean;
    createdAt: string;
    updatedAt: string;
    size: number;
    scarCount: number;
    forksCount: number;
    watchersCount: number;
  };
  languages: {
    [key: string]: number;
  };
  versions: Array<{
    name: string;
    commit: string;
    zipball: string;
    tarball: string;
  }>;
  contributors: Array<{
    username: string;
    avatar: string;
    contributions: number;
  }>;
  commits: Array<{
    sha: string;
    authorName: string;
    authorDate: string;
    message: string;
    authorUsername: string;
    authorAvatar: string;
  }>;
}
