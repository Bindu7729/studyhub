"""
StudyHub PDF Document Metadata and Text Inspector.
"""
from typing import Dict, Any


def inspect_document_stats(filename: str, byte_size: int, page_count: int = 1) -> Dict[str, Any]:
    if not filename:
        return {"filename": "", "extension": "", "size_mb": 0.0, "is_valid": False}

    ext = filename.split(".")[-1].lower() if "." in filename else ""
    size_mb = round(byte_size / (1024 * 1024), 2)
    is_valid = ext in ["pdf", "epub", "docx", "txt"] and byte_size > 0 and byte_size <= 50 * 1024 * 1024

    read_time_mins = max(1, round(page_count * 2.5))

    return {
        "filename": filename,
        "extension": ext,
        "size_mb": size_mb,
        "page_count": max(1, page_count),
        "read_time_mins": read_time_mins,
        "is_valid": is_valid
    }
