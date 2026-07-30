from app.services.search_indexer import InvertedIndex


def test_inverted_index_indexing_and_search():
    idx = InvertedIndex()
    idx.add_document("doc1", "Dynamic programming memoization algorithms")
    idx.add_document("doc2", "Graph search breadth first search")
    idx.add_document("doc3", "Dynamic graph flow algorithms")

    res = idx.search("dynamic algorithms")
    assert "doc1" in res
    assert "doc3" in res
    assert "doc2" not in res
