export interface StudyGoal {
  targetMinutes: number;
  completedMinutes: number;
  streakDays: number;
}

export function evaluateGoalProgress(goal: StudyGoal): { percentComplete: number; isGoalMet: boolean; remainingMinutes: number } {
  const percentComplete = goal.targetMinutes > 0
    ? Math.min(100, Math.round((goal.completedMinutes / goal.targetMinutes) * 100))
    : 100;

  const remainingMinutes = Math.max(0, goal.targetMinutes - goal.completedMinutes);

  return {
    percentComplete,
    isGoalMet: goal.completedMinutes >= goal.targetMinutes,
    remainingMinutes
  };
}
