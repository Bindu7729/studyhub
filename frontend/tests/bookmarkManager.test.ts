import { describe, it, expect } from 'vitest';
import { toggleBookmark } from '../lib/bookmarkManager';

describe('Bookmark Manager Utility', () => {
  it('adds new bookmarks when not present and removes when already bookmarked', () => {
    let list = toggleBookmark([], { id: 'item1', title: 'DSA Pack', category: 'DSA' });
    expect(list).toHaveLength(1);
    expect(list[0].id).toBe('item1');

    list = toggleBookmark(list, { id: 'item1', title: 'DSA Pack', category: 'DSA' });
    expect(list).toHaveLength(0); // Toggled off
  });
});
