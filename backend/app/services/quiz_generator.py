"""
StudyHub Quiz Question Bank Sampler & Randomizer Service.
"""
import random
from typing import List, Dict, Any


def sample_quiz_questions(question_bank: List[Dict[str, Any]], sample_size: int = 10, seed: int = None) -> List[Dict[str, Any]]:
    """
    Deterministically or randomly samples a subset of practice questions.
    """
    if not question_bank:
        return []

    if sample_size <= 0:
        return []

    count = min(sample_size, len(question_bank))
    rng = random.Random(seed) if seed is not None else random.Random()
    return rng.sample(question_bank, count)
