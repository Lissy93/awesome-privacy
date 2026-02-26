export const fetchDiscordInfo = async (
  discordInvite: string,
): Promise<DiscordInfo | null> => {
  const endpoint = `https://discord-invite-info.as93.net/${discordInvite}`;
  try {
    return await fetch(endpoint).then((res) => res.json());
  } catch (error) {
    console.error('Error fetching discord data:', error);
    return null;
  }
};

export interface DiscordInfo {
  inviteCode: string;
  name: string;
  memberCount: number;
  memberOnlineCount: number;
  channel: string;
  icon: string;
  banner: string;
  inviter: string | null;
}
