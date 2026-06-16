"""
StudyHub Spaced Repetition Flashcard Engine (SM-2 Algorithm).
Calculates review intervals and ease factor adjustments.
"""
from typing import Dict, Any


def calculate_sm2_review(ease_factor: float, interval_days: int, repetitions: int, grade: int) -> Dict[str, Any]:
    """
    Computes new interval and ease factor based on user recall grade (0-5).
    grade >= 3 indicates correct recall.
    """
    grade = max(0, min(5, grade))

    if grade >= 3:
        if repetitions == 0:
            new_interval = 1
        elif repetitions == 1:
            new_interval = 6
        else:
            new_interval = round(interval_days * ease_factor)
        new_repetitions = repetitions + 1
    else:
        new_repetitions = 0
        new_interval = 1

    # Update ease factor
    new_ease = ease_factor + (0.1 - (5 - grade) * (0.08 + (5 - grade) * 0.02))
    new_ease = max(1.3, new_ease)

    return {
        "ease_factor": round(new_ease, 2),
        "interval_days": new_interval,
        "repetitions": new_repetitions,
        "is_mastered": new_repetitions >= 5
    }
