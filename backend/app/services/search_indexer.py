"""
Inverted Index Search Service for StudyHub Study Materials.
"""
from typing import Dict, List, Set
from collections import defaultdict
import re


class InvertedIndex:
    def __init__(self):
        self.index: Dict[str, Set[str]] = defaultdict(set)

    def add_document(self, doc_id: str, text: str):
        tokens = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
        for token in tokens:
            self.index[token].add(doc_id)

    def search(self, query: str) -> List[str]:
        tokens = re.findall(r'\b[a-zA-Z]{3,}\b', query.lower())
        if not tokens:
            return []

        # Intersect matches
        res = self.index.get(tokens[0], set()).copy()
        for t in tokens[1:]:
            res &= self.index.get(t, set())

        return sorted(list(res))
