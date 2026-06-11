"""
Unit tests for StudyHub Pomodoro study session timer service.
"""
from app.services.study_timer import calculate_study_session_schedule


def test_calculate_study_session_schedule_standard():
    schedule = calculate_study_session_schedule(100, focus_block_minutes=25, short_break_minutes=5, long_break_minutes=15)
    assert schedule["focus_blocks"] == 4
    assert schedule["long_breaks"] == 1
    assert schedule["short_breaks"] == 2
    assert schedule["total_break_minutes"] == (2 * 5) + (1 * 15)  # 25 minutes break
    assert schedule["total_time_minutes"] == 125


def test_calculate_study_session_schedule_zero():
    schedule = calculate_study_session_schedule(0)
    assert schedule["focus_blocks"] == 0
    assert schedule["total_time_minutes"] == 0
