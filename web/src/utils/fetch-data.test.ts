import { describe, it, expect } from 'vitest';
import { slugify } from './fetch-data';

describe('slugify', () => {
  it('lowercases and replaces spaces with hyphens', () => {
    expect(slugify('Hello World')).toBe('hello-world');
  });

  it('replaces & with "and"', () => {
    expect(slugify('Privacy & Security')).toBe('privacy-and-security');
  });

  it('replaces + with "and"', () => {
    expect(slugify('Tools + Tips')).toBe('tools-and-tips');
  });

  it('removes question marks', () => {
    expect(slugify('What is Privacy?')).toBe('what-is-privacy');
  });

  it('handles multiple spaces', () => {
    expect(slugify('a  b   c')).toBe('a--b---c');
  });

  it('returns empty string for empty input', () => {
    expect(slugify('')).toBe('');
  });

  it('returns empty string for undefined-like input', () => {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    expect(slugify(undefined as any)).toBe('');
  });

  it('handles combined special characters', () => {
    expect(slugify('Q&A + FAQ?')).toBe('qanda-and-faq');
  });
});
