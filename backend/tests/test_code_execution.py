"""Unit tests for the isolated code execution service."""
import pytest
from app.services.code_execution_service import CodeExecutionService


@pytest.fixture
def execution_service():
    return CodeExecutionService()


def test_python_successful_execution(execution_service: CodeExecutionService):
    result = execution_service.execute_project(
        language="python",
        files=[{"path": "main.py", "content": "print('Hello StudyHub')"}]
    )
    assert result["status"] == "accepted"
    assert "Hello StudyHub" in result["stdout"]
    assert result["compileError"] is None
    assert result["executionTime"] >= 0.0


def test_python_stdin_processing(execution_service: CodeExecutionService):
    result = execution_service.execute_project(
        language="python",
        files=[{"path": "main.py", "content": "val = input()\nprint(f'Echo: {val}')"}],
        stdin="StudyHubTester"
    )
    assert result["status"] == "accepted"
    assert "Echo: StudyHubTester" in result["stdout"]


def test_python_runtime_error(execution_service: CodeExecutionService):
    result = execution_service.execute_project(
        language="python",
        files=[{"path": "main.py", "content": "x = 1 / 0"}]
    )
    assert result["status"] == "runtime_error"
    assert "ZeroDivisionError" in result["stderr"]


def test_unsupported_language(execution_service: CodeExecutionService):
    result = execution_service.execute_project(
        language="unsupported_lang_xyz",
        files=[{"path": "main.xyz", "content": "code"}]
    )
    assert result["status"] == "error"
    assert "Unsupported language" in result["stderr"]


def test_python_timeout_termination(execution_service: CodeExecutionService):
    # Test infinite loop termination
    result = execution_service.execute_project(
        language="python",
        files=[{"path": "main.py", "content": "import time\nwhile True:\n    time.sleep(0.1)"}]
    )
    assert result["status"] == "timeout"
    assert "Time Limit Exceeded" in result["stderr"]
