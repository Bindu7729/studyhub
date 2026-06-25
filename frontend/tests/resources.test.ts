import { describe, it, expect } from 'vitest';
import { RESOURCE_CATALOG, resourceService } from '../lib/resources';

describe('StudyHub Resource Catalog Suite', () => {
  it('contains valid study bundles and academic resources', () => {
    expect(RESOURCE_CATALOG.length).toBeGreaterThan(10);
    const dsaPack = RESOURCE_CATALOG.find(r => r.id === 'aads-pack');
    expect(dsaPack).toBeDefined();
    expect(dsaPack?.type).toBe('PACK');
    expect(dsaPack?.difficulty).toBe('Advanced');
  });

  it('filters catalog items by category and search keywords', () => {
    const dsaItems = resourceService.searchAndFilter({ category: 'DSA' });
    expect(dsaItems.length).toBeGreaterThan(0);
    expect(dsaItems.every(r => r.category === 'DSA')).toBe(true);

    const algoSearch = resourceService.searchAndFilter({ query: 'Algorithms' });
    expect(algoSearch.length).toBeGreaterThan(0);
  });

  it('sorts catalog items alphabetically A-Z and by difficulty', () => {
    const sortedAZ = resourceService.searchAndFilter({ sortBy: 'A-Z' });
    expect(sortedAZ[0].title.localeCompare(sortedAZ[1].title)).toBeLessThanOrEqual(0);

    const sortedDiff = resourceService.searchAndFilter({ sortBy: 'Difficulty' });
    expect(sortedDiff[0].difficulty).toBe('Beginner');
  });
});
