import { describe, it, expect } from 'vitest';
import { cn, formatDistanceToNow } from '../lib/utils';

describe('StudyHub Frontend Utility Suite', () => {
  describe('cn (clsx wrapper)', () => {
    it('combines conditional and truthy class names safely', () => {
      expect(cn('btn', true && 'btn-primary', false && 'btn-danger')).toBe('btn btn-primary');
      expect(cn('p-4', undefined, null, 'text-center')).toBe('p-4 text-center');
    });
  });

  describe('formatDistanceToNow', () => {
    it('formats relative elapsed time accurately', () => {
      const now = Date.now();
      expect(formatDistanceToNow(new Date(now - 10000))).toBe('just now');
      expect(formatDistanceToNow(new Date(now - 120000))).toBe('2m ago');
      expect(formatDistanceToNow(new Date(now - 7200000))).toBe('2h ago');
    });
  });
});
