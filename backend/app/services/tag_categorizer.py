"""
Automatic Tag Categorizer Service.
"""
from typing import List, Dict


CATEGORY_KEYWORDS: Dict[str, List[str]] = {
    "DSA": ["algorithm", "tree", "graph", "sort", "search", "stack", "queue", "heap", "complexity"],
    "Database": ["sql", "query", "table", "schema", "postgres", "mysql", "index", "acid", "relation"],
    "Web": ["react", "html", "css", "javascript", "frontend", "backend", "api", "rest", "http"],
    "Systems": ["network", "socket", "tcp", "udp", "thread", "memory", "os", "kernel", "concurrency"]
}


import re

def suggest_categories(text: str) -> List[str]:
    lower_text = text.lower()
    matches = []
    for cat, keywords in CATEGORY_KEYWORDS.items():
        if any(re.search(r'\b' + re.escape(kw) + r'\b', lower_text) for kw in keywords):
            matches.append(cat)
    return matches if matches else ["General"]
