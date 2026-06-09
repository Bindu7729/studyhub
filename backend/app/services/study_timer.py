"""
StudyHub Pomodoro Study Session Timer Service
Manages study cycles, rest intervals, and productivity tracking.
"""
from typing import Dict, Any


def calculate_study_session_schedule(total_study_minutes: int, focus_block_minutes: int = 25, short_break_minutes: int = 5, long_break_minutes: int = 15) -> Dict[str, Any]:
    """
    Computes pomodoro study blocks and recommended break intervals.
    """
    if total_study_minutes <= 0:
        return {
            "total_study_minutes": 0,
            "focus_blocks": 0,
            "short_breaks": 0,
            "long_breaks": 0,
            "total_break_minutes": 0,
            "total_time_minutes": 0
        }

    focus_blocks = total_study_minutes // focus_block_minutes
    if total_study_minutes % focus_block_minutes != 0:
        focus_blocks += 1

    long_breaks = focus_blocks // 4
    short_breaks = max(0, focus_blocks - 1 - long_breaks)

    total_break_minutes = (short_breaks * short_break_minutes) + (long_breaks * long_break_minutes)

    return {
        "total_study_minutes": total_study_minutes,
        "focus_blocks": focus_blocks,
        "short_breaks": short_breaks,
        "long_breaks": long_breaks,
        "total_break_minutes": total_break_minutes,
        "total_time_minutes": total_study_minutes + total_break_minutes
    }
