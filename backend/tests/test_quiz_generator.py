"""
Unit tests for StudyHub quiz question sampler.
"""
from app.services.quiz_generator import sample_quiz_questions


def test_sample_quiz_questions_reproducible_with_seed():
    bank = [{"id": i, "question": f"Q{i}"} for i in range(20)]
    sample_a = sample_quiz_questions(bank, sample_size=5, seed=42)
    sample_b = sample_quiz_questions(bank, sample_size=5, seed=42)

    assert len(sample_a) == 5
    assert sample_a == sample_b


def test_sample_quiz_questions_exceeding_bank_size():
    bank = [{"id": 1, "question": "Q1"}]
    sample = sample_quiz_questions(bank, sample_size=10)
    assert len(sample) == 1
