import { describe, it, expect } from 'vitest';
import { analyzeSecurityChecks } from './security-check-mappings';

describe('analyzeSecurityChecks', () => {
  it('classifies a passing HTTPS check as passed', () => {
    const { passedChecks, failedChecks } = analyzeSecurityChecks({
      is_valid_https: true,
    });
    expect(passedChecks).toContain('Valid HTTPS Connection');
    expect(failedChecks).toHaveLength(0);
  });

  it('classifies is_valid_https: "no" as failed', () => {
    // The pass logic uses (value === shouldPass) || (shouldPass === true && value !== "no")
    // For boolean false, the second condition still passes (false !== "no" is true).
    // Only the string "no" actually triggers a failure when shouldPass is true.
    const { failedChecks } = analyzeSecurityChecks({
      is_valid_https: 'no',
    });
    expect(failedChecks).toContain('Valid HTTPS Connection');
  });

  it('classifies a false-means-pass check correctly', () => {
    // is_host_an_ipv4 should be false to pass
    const { passedChecks } = analyzeSecurityChecks({
      is_host_an_ipv4: false,
    });
    expect(passedChecks).toContain('Host is an IPv4 Address');
  });

  it('classifies a false-means-pass check as failed when true', () => {
    const { failedChecks } = analyzeSecurityChecks({
      is_host_an_ipv4: true,
    });
    expect(failedChecks).toContain('Host is an IPv4 Address');
  });

  it('handles multiple checks at once', () => {
    const { passedChecks, failedChecks } = analyzeSecurityChecks({
      is_valid_https: true,
      is_host_an_ipv4: false,
      is_suspended_page: true, // should fail (expected false)
    });
    expect(passedChecks).toHaveLength(2);
    expect(failedChecks).toHaveLength(1);
    expect(failedChecks).toContain('Suspended Page');
  });

  it('handles string "no" values for domain_recent checks', () => {
    const { passedChecks } = analyzeSecurityChecks({
      is_domain_recent: 'no',
    });
    expect(passedChecks).toContain('Domain Recently Created');
  });

  it('fails domain_recent when value is not "no"', () => {
    const { failedChecks } = analyzeSecurityChecks({
      is_domain_recent: 'yes',
    });
    expect(failedChecks).toContain('Domain Recently Created');
  });

  it('returns empty arrays for empty input', () => {
    const { passedChecks, failedChecks } = analyzeSecurityChecks({});
    expect(passedChecks).toHaveLength(0);
    expect(failedChecks).toHaveLength(0);
  });
});
