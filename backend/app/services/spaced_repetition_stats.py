"""
Ebbinghaus Forgetting Curve and Retention Decay Calculator.
"""
import math
from typing import Dict, Any


def calculate_retention_probability(elapsed_days: float, stability: float = 2.0) -> float:
    """
    R = e^(-t / S) where t is elapsed days and S is memory stability.
    """
    if elapsed_days <= 0:
        return 1.0
    if stability <= 0:
        return 0.0

    retention = math.exp(-elapsed_days / stability)
    return round(retention, 4)
