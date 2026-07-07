import { describe, it, expect } from 'vitest';

export interface StudyTracker {
  activeSubject: string;
  elapsedSeconds: number;
  completedTasks: string[];
}

export function createStudyTracker(subject: string): StudyTracker {
  return {
    activeSubject: subject,
    elapsedSeconds: 0,
    completedTasks: []
  };
}

export function logCompletedTask(tracker: StudyTracker, taskTitle: string): StudyTracker {
  return {
    ...tracker,
    completedTasks: [...tracker.completedTasks, taskTitle]
  };
}

describe('Study Session Tracker', () => {
  it('initializes new study tracker with zero elapsed time', () => {
    const tracker = createStudyTracker('Data Structures');
    expect(tracker.activeSubject).toBe('Data Structures');
    expect(tracker.elapsedSeconds).toBe(0);
    expect(tracker.completedTasks).toHaveLength(0);
  });

  it('records completed study milestone tasks', () => {
    let tracker = createStudyTracker('Algorithms');
    tracker = logCompletedTask(tracker, 'Solve 3 Dynamic Programming problems');
    tracker = logCompletedTask(tracker, 'Review Bellman-Ford shortest paths');

    expect(tracker.completedTasks).toHaveLength(2);
    expect(tracker.completedTasks[0]).toBe('Solve 3 Dynamic Programming problems');
  });
});
