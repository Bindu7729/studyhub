import { describe, it, expect } from 'vitest';
import { evaluateGoalProgress } from '../lib/studyGoals';

describe('Study Goal Evaluation Utility', () => {
  it('computes completion percent and remaining minutes', () => {
    const goal = { targetMinutes: 120, completedMinutes: 90, streakDays: 5 };
    const res = evaluateGoalProgress(goal);

    expect(res.percentComplete).toBe(75);
    expect(res.remainingMinutes).toBe(30);
    expect(res.isGoalMet).toBe(false);
  });

  it('marks goal as met when completed minutes exceed target', () => {
    const goal = { targetMinutes: 60, completedMinutes: 80, streakDays: 6 };
    const res = evaluateGoalProgress(goal);

    expect(res.percentComplete).toBe(100);
    expect(res.isGoalMet).toBe(true);
    expect(res.remainingMinutes).toBe(0);
  });
});
