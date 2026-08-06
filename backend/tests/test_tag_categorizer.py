from app.services.tag_categorizer import suggest_categories


def test_suggest_categories_matches_keywords():
    cats = suggest_categories("Binary Search Tree and Heap Complexity")
    assert "DSA" in cats

    web_cats = suggest_categories("Full stack REST API with React frontend")
    assert "Web" in web_cats


def test_suggest_categories_fallback():
    assert suggest_categories("Random prose without tech terms") == ["General"]
