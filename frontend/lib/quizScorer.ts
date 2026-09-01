export interface QuizAnswer {
  questionId: string;
  selectedOption: number;
  correctOption: number;
  timeTakenSeconds: number;
}

export function scoreQuizSession(answers: QuizAnswer[]): { score: number; maxScore: number; accuracy: number; avgTimeSec: number } {
  if (!answers || answers.length === 0) {
    return { score: 0, maxScore: 0, accuracy: 0, avgTimeSec: 0 };
  }

  let correct = 0;
  let totalTime = 0;

  for (const a of answers) {
    totalTime += a.timeTakenSeconds || 0;
    if (a.selectedOption === a.correctOption) {
      correct++;
    }
  }

  const accuracy = Math.round((correct / answers.length) * 100);
  const score = correct * 10;
  const maxScore = answers.length * 10;
  const avgTimeSec = Math.round(totalTime / answers.length);

  return {
    score,
    maxScore,
    accuracy,
    avgTimeSec
  };
}
