
export const fetchRedditInfo = async (subreddit: string): Promise<RedditData | null> => {
  const endpoint = `https://subreddit-info.as93.net/${subreddit}`;
  try {
    return await fetch(endpoint).then((res) => res.json());
  } catch (error) {
    console.error('Error fetching reddit data:', error);
    return null;
  }
};

interface SubredditInfo {
  name: string | null;
  title: string | null;
  description: string | null;
  longDescription: string | null;
  icon: string | null;
  banner: string | null;
  color: string | null;
  subscribers: number | null;
  activeSubscribers: number | null;
  dateCreated: number | null;
  descriptionHtml: string | null;
}

interface Post {
  title: string;
  body: string;
  upVotes: number;
  downVotes: number;
  date: number;
  url: string;
}

export interface RedditData {
  info: SubredditInfo;
  posts: Post[];
}
