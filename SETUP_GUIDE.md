# StudyHub — Full-Stack Setup & Local Development Guide

StudyHub is an engineering placement preparation and technical learning platform built as a decoupled full-stack application: Next.js 16 (App Router) on the frontend and FastAPI (async Python 3.12) on the backend.

---

## 1. Prerequisites

- **Node.js**: v20+ (recommended v22+)
- **Python**: v3.12+
- **Git**: Installed and configured

---

## 2. Repository Architecture

```
StudyHub/
├── backend/                  # FastAPI Application
│   ├── app/
│   │   ├── api/routes/       # REST API Endpoints (12 route modules)
│   │   ├── core/             # Database, config, security, exceptions, middleware
│   │   ├── models/           # SQLAlchemy async models (46 tables)
│   │   ├── schemas/          # Pydantic validation schemas
│   │   └── services/         # Execution sandbox, resume parser, community
│   ├── tests/                # PyTest automated test suite
│   ├── pathward.db           # Pre-seeded SQLite database (437 topics, 11 companies)
│   └── requirements.txt      # Python dependencies
├── frontend/                 # Next.js 16 Web Application
│   ├── app/                  # App Router pages (/practice, /learn, /dashboard, etc.)
│   ├── components/           # Modular UI & landing section components
│   ├── lib/                  # Centralized API client, storage, and utilities
│   └── types/                # Shared TypeScript interfaces
├── .github/workflows/        # Automated CI/CD pipelines
├── package.json              # Monorepo unified commands
└── README.md                 # Project showcase and overview
```

---

## 3. Quick Start (Development Mode)

### Step A: Backend Setup

```bash
cd backend

# 1. Create and activate virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env

# 4. Start the FastAPI development server
uvicorn app.main:app --reload --port 8000
```

Verify backend health at: [http://localhost:8000/health](http://localhost:8000/health)  
Interactive OpenAPI documentation: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### Step B: Frontend Setup

Open a new terminal window:

```bash
cd frontend

# 1. Install dependencies
npm install

# 2. Configure environment
cp .env.example .env.local

# 3. Start Next.js development server
npm run dev
```

Open the web app at: [http://localhost:3000](http://localhost:3000)

---

## 4. Running Automated Tests

### Backend Test Suite
From the `backend` directory (with virtualenv active):
```bash
pytest -v tests
```
The suite runs unit and integration tests covering:
- API health and database connectivity
- Multi-language sandbox code execution with timeout guarantees
- Practice problem filtering, search, and 404 boundaries
- Resume text parsing and ATS section extraction

---

## 5. Key API Endpoints Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Health check with database connectivity probe and latency metrics |
| `GET` | `/api/practice/sets` | Practice problem sets with domain and difficulty filtering |
| `GET` | `/api/practice/sets/{id}` | Problem set details and question catalog |
| `POST` | `/api/execution/run` | Execute user code in isolated subprocess sandbox |
| `POST` | `/api/execution/submit` | Submit code against visible and hidden test cases |
| `GET` | `/api/community/feed` | Community forum activity and posts |
| `GET` | `/api/community/posts/{id}/comments` | Post comments with chronological sorting |
| `POST` | `/api/resume/analyses` | PDF resume upload and ATS score extraction |
| `GET` | `/api/learn/tree` | Full curriculum topic hierarchy (437 topics) |

---

## 6. Security & Sandboxing

The backend code execution engine runs user-submitted code in an isolated temporary directory with:
- Strict process execution time ceiling (`TIMEOUT_SECONDS = 6.0`)
- Sanitized environment variables (`PATH`, `SYSTEMROOT` only; parents secrets are masked)
- Directory traversal prevention
- Automatic zombie process termination
