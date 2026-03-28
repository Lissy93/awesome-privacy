import { describe, it, expect } from 'vitest';
import { formatLink } from './parse-markdown';

describe('formatLink', () => {
  it('strips https://', () => {
    expect(formatLink('https://example.com')).toBe('example.com');
  });

  it('strips http://', () => {
    expect(formatLink('http://example.com')).toBe('example.com');
  });

  it('strips www.', () => {
    expect(formatLink('https://www.example.com')).toBe('example.com');
  });

  it('strips trailing slash', () => {
    expect(formatLink('https://example.com/')).toBe('example.com');
  });

  it('strips multiple trailing slashes', () => {
    expect(formatLink('https://example.com///')).toBe('example.com');
  });

  it('preserves path segments', () => {
    expect(formatLink('https://example.com/path/to/page')).toBe(
      'example.com/path/to/page',
    );
  });

  it('handles bare domain', () => {
    expect(formatLink('example.com')).toBe('example.com');
  });

  it('handles empty string', () => {
    expect(formatLink('')).toBe('');
  });

  it('handles undefined-like input', () => {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    expect(formatLink(undefined as any)).toBe('');
  });
});
