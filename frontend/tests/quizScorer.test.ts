import { describe, it, expect } from 'vitest';
import { scoreQuizSession } from '../lib/quizScorer';

describe('Quiz Session Scoring Utility', () => {
  it('calculates score, accuracy, and average response latency', () => {
    const answers = [
      { questionId: 'q1', selectedOption: 1, correctOption: 1, timeTakenSeconds: 15 },
      { questionId: 'q2', selectedOption: 2, correctOption: 3, timeTakenSeconds: 25 },
      { questionId: 'q3', selectedOption: 0, correctOption: 0, timeTakenSeconds: 20 }
    ];

    const result = scoreQuizSession(answers);

    expect(result.score).toBe(20);
    expect(result.maxScore).toBe(30);
    expect(result.accuracy).toBe(67);
    expect(result.avgTimeSec).toBe(20);
  });
});
