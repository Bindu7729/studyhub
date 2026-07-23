from app.services.pdf_extractor import inspect_document_stats


def test_inspect_document_stats_valid_pdf():
    stats = inspect_document_stats("Algorithms_Vol1.pdf", 1048576 * 5, page_count=20)
    assert stats["extension"] == "pdf"
    assert stats["size_mb"] == 5.0
    assert stats["is_valid"] is True
    assert stats["read_time_mins"] == 50


def test_inspect_document_stats_invalid_extension():
    stats = inspect_document_stats("exploit.exe", 100)
    assert stats["is_valid"] is False
