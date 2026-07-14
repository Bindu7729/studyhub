"""
StudyHub Notes Keypoint Extractor and Summarizer Service.
"""
import re
from typing import List, Dict, Any


def extract_key_points(text: str, max_points: int = 5) -> List[str]:
    """
    Extracts key conceptual sentences based on significance keywords and formatting.
    """
    if not text or not text.strip():
        return []

    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    importance_keywords = ['important', 'key', 'essential', 'must', 'core', 'crucial', 'fundamental', 'concept', 'note', 'definition']

    scored_sentences = []
    for s in sentences:
        s_clean = s.strip()
        if len(s_clean) < 15:
            continue
        score = sum(1 for kw in importance_keywords if kw in s_clean.lower())
        scored_sentences.append((score, s_clean))

    # Sort descending by score while preserving top ones
    scored_sentences.sort(key=lambda x: x[0], reverse=True)
    return [s[1] for s in scored_sentences[:max_points]]
