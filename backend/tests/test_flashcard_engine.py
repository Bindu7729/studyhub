"""
Unit tests for SM-2 spaced repetition flashcard scheduler.
"""
from app.services.flashcard_engine import calculate_sm2_review


def test_first_successful_recall():
    res = calculate_sm2_review(ease_factor=2.5, interval_days=0, repetitions=0, grade=5)
    assert res["repetitions"] == 1
    assert res["interval_days"] == 1
    assert res["ease_factor"] >= 2.5


def test_second_successful_recall():
    res = calculate_sm2_review(ease_factor=2.5, interval_days=1, repetitions=1, grade=4)
    assert res["repetitions"] == 2
    assert res["interval_days"] == 6


def test_failed_recall_resets_streak():
    res = calculate_sm2_review(ease_factor=2.5, interval_days=12, repetitions=3, grade=1)
    assert res["repetitions"] == 0
    assert res["interval_days"] == 1
    assert res["ease_factor"] < 2.5
