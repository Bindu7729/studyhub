"""
Unit tests for notes summarizer service.
"""
from app.services.notes_summarizer import extract_key_points


def test_extract_key_points_identifies_crucial_concepts():
    text = (
        "This is an introductory sentence. "
        "The core concept of dynamic programming is memoization and optimal substructure. "
        "Another essential rule is avoiding redundant recursive calls. "
        "Filler sentence with very little relevance."
    )
    points = extract_key_points(text, max_points=2)
    assert len(points) == 2
    assert any("dynamic programming" in p for p in points)


def test_extract_key_points_empty_text():
    assert extract_key_points("") == []
    assert extract_key_points("   ") == []
