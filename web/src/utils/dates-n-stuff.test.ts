import { describe, it, expect } from 'vitest';
import { formatDate, timestampToDate } from './dates-n-stuff';

describe('formatDate', () => {
  it('formats an ISO date string to en-GB short format', () => {
    const result = formatDate('2024-01-15');
    expect(result).toBe('15 Jan 24');
  });

  it('formats a different date correctly', () => {
    const result = formatDate('2023-12-25');
    expect(result).toBe('25 Dec 23');
  });

  it('handles full ISO datetime string', () => {
    const result = formatDate('2024-06-01T12:00:00Z');
    expect(result).toBe('01 Jun 24');
  });
});

describe('timestampToDate', () => {
  it('converts a Unix timestamp (ms) to en-GB short format', () => {
    // 2024-01-15T00:00:00Z = 1705276800000
    const result = timestampToDate(1705276800000);
    expect(result).toBe('15 Jan 24');
  });

  it('converts epoch 0 to 01 Jan 70', () => {
    const result = timestampToDate(0);
    expect(result).toBe('01 Jan 70');
  });
});
