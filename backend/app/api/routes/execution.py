from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, Any
import subprocess

from app.services.execution_service import execute_java, execute_python, execute_cpp, ExecutionRequest, ExecutionResult, TestCase
from app.services.problem_registry import get_hidden_tests
from app.services.groq_service import explain_code_error
from app.core.security import get_current_user

class ExplainErrorRequest(BaseModel):
    code: str
    error_message: str
    language: str

router = APIRouter(
    prefix="/api/execution",
    tags=["Execution"]
)


def route_execution(request: ExecutionRequest) -> ExecutionResult:
    lang = request.functionSignature.language.lower()
    if lang == "java":
        return execute_java(request)
    elif lang == "python":
        return execute_python(request)
    elif lang == "cpp":
        return execute_cpp(request)
    else:
        raise HTTPException(status_code=400, detail=f"Unsupported language: {lang}")


@router.post("/run", response_model=ExecutionResult)
async def run_code(request: ExecutionRequest):
    return route_execution(request)


@router.post("/submit", response_model=ExecutionResult)
async def submit_code(request: ExecutionRequest):
    # Append hidden tests for submission
    hidden_tests = get_hidden_tests(request.problemId)
    for ht in hidden_tests:
        request.testCases.append(TestCase(**ht))

    result = route_execution(request)
    
    if result.status == "accepted" and request.userId:
        try:
            from app.core.database import AsyncSessionLocal
            from app.models.roadmap import UserDSAProblemProgress
            from sqlalchemy.future import select
            from datetime import datetime

            async with AsyncSessionLocal() as session:
                stmt = select(UserDSAProblemProgress).where(
                    UserDSAProblemProgress.user_id == request.userId,
                    UserDSAProblemProgress.problem_id == request.problemId
                )
                res = await session.execute(stmt)
                prog = res.scalars().first()
                now = datetime.utcnow()

                if prog:
                    prog.attempts = (prog.attempts or 0) + 1
                    prog.status = "solved"
                    prog.solved_at = now
                    prog.attempted_at = now
                else:
                    new_prog = UserDSAProblemProgress(
                        id=f"{request.userId}_{request.problemId}",
                        user_id=request.userId,
                        problem_id=request.problemId,
                        status="solved",
                        attempts=1,
                        solved_at=now,
                        attempted_at=now
                    )
                    session.add(new_prog)
                await session.commit()
        except Exception:
            pass

    return result

@router.post("/explain-error")
async def explain_error(request: ExplainErrorRequest):
    try:
        explanation = await explain_code_error(request.code, request.error_message, request.language)
        return {"explanation": explanation}
    except ValueError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to generate explanation.")
