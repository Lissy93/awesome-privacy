export const formatDate = (date: string): string => {
  return new Date(date).toLocaleDateString('en-GB', {
    day: '2-digit',
    month: 'short',
    year: '2-digit'
  });
}

export const timestampToDate = (timestamp: number): string => {
  return new Date(timestamp).toLocaleDateString('en-GB', {
    day: '2-digit',
    month: 'short',
    year: '2-digit'
  });

}

export const timeAgo = (dateStr: string): string => {
  const seconds = Math.floor((new Date().getTime() - new Date(dateStr).getTime()) / 1000);
  const intervals = {
    year: 31536000,
    month: 2592000,
    day: 86400,
    hour: 3600,
    minute: 60,
  };
  for (const [key, value] of Object.entries(intervals)) {
    const count = Math.floor(seconds / value);
    if (count > 0) return `${count} ${key}${count !== 1 ? 's' : ''} ago`;
  }
  return 'just now';
};
