from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.core.config import settings
from app.core.database import engine, Base
from app.core.exceptions import (
    StudyHubException,
    studyhub_exception_handler,
    http_exception_handler,
    validation_exception_handler,
)
from app.core.middleware import RequestLoggingMiddleware

app = FastAPI(
    title=settings.app_name,
    description="Backend API for StudyHub placement preparation platform",
    version=settings.app_version,
)

app.add_exception_handler(StudyHubException, studyhub_exception_handler)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

from app.models import company, daily_plans, learning, practice, profile, resource, roadmap, templates, tools, settings as user_settings_model, community, resume_analysis
from sqlalchemy import text

def sync_table_columns(connection):
    for table_name, table in Base.metadata.tables.items():
        try:
            result = connection.execute(text(f"PRAGMA table_info({table_name})"))
            db_cols = {row[1] for row in result.fetchall()}
            if not db_cols:
                continue
            for col in table.columns:
                if col.name not in db_cols:
                    col_type = col.type.compile(connection.dialect)
                    connection.execute(text(f"ALTER TABLE {table_name} ADD COLUMN {col.name} {col_type}"))
        except Exception:
            pass

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        # Create all tables (safe because it only creates tables that don't exist yet)
        await conn.run_sync(Base.metadata.create_all)
        # Sync any newly added columns in models
        await conn.run_sync(sync_table_columns)

from app.api.routes import profile, dashboard, learn, ai, resources, roadmaps, practice, community, resume, execution

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_origin_regex=r"https?://(localhost|127\.0\.0\.1)(:\d+)?",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)
app.add_middleware(RequestLoggingMiddleware)

app.include_router(profile.router)
app.include_router(dashboard.router)
app.include_router(learn.router)
app.include_router(ai.router)
app.include_router(resources.router)
app.include_router(roadmaps.router)
app.include_router(practice.router)
app.include_router(community.router)
app.include_router(resume.router)
app.include_router(execution.router)

@app.get("/")

async def root():
    return {"message": "Welcome to StudyHub API"}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "environment": settings.environment,
        "version": "1.0.0"
    }
