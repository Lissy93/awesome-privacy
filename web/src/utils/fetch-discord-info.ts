import { error } from './logger';

export const fetchDiscordInfo = async (
  discordInvite: string,
): Promise<DiscordInfo | null> => {
  const endpoint = `https://discord-invite-info.as93.net/${discordInvite}`;
  try {
    const res = await fetch(endpoint);
    if (!res.ok) {
      error('Discord', `HTTP ${res.status} for ${discordInvite} (${endpoint})`);
      return null;
    }
    return await res.json();
  } catch (err) {
    error('Discord', `Network error for ${discordInvite}: ${err}`);
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
