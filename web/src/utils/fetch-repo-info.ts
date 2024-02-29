


export const fetchGitHubStats = async (github: string): Promise<GitHubStatsResponse | null> => {
  const endpoint = `https://repo-info.as93.workers.dev/${github}`;
  try {
    return await fetch(endpoint).then((res) => res.json());
  } catch (error) {
    console.error('Error fetching GitHub stats:', error);
    return null;
  }
};

// fetch(`https://repo-info.as93.workers.dev/${github}`).then((res) => res.json());

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
  updates: Array<{
    type: string;
    actor: {
      username: string;
      avatar: string;
    };
    repo: string;
    action: string;
    createdAt: string;
    number?: number;
  }>;
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
