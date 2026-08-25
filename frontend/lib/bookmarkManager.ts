export interface BookmarkItem {
  id: string;
  title: string;
  category: string;
  savedAt: number;
}

export function toggleBookmark(bookmarks: BookmarkItem[], item: { id: string; title: string; category: string }): BookmarkItem[] {
  const exists = bookmarks.some(b => b.id === item.id);
  if (exists) {
    return bookmarks.filter(b => b.id !== item.id);
  }
  return [...bookmarks, { ...item, savedAt: Date.now() }];
}
