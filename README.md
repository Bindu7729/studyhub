# StudyHub — Placement Preparation & Technical Learning Platform

[![Backend CI](https://github.com/Bindu7729/studyhub/actions/workflows/backend-ci.yml/badge.svg)](https://github.com/Bindu7729/studyhub/actions/workflows/backend-ci.yml)
[![Frontend CI](https://github.com/Bindu7729/studyhub/actions/workflows/frontend-ci.yml/badge.svg)](https://github.com/Bindu7729/studyhub/actions/workflows/frontend-ci.yml)
![Next.js 16](https://img.shields.io/badge/Next.js-16-black?logo=next.js)
![React 19](https://img.shields.io/badge/React-19-blue?logo=react)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-009688?logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python)
![TypeScript](https://img.shields.io/badge/TypeScript-5+-3178C6?logo=typescript)

A comprehensive placement-preparation and technical-learning platform for engineering students: **Learn → Practice → Prepare → Build → Apply → Interview**.

StudyHub combines an interactive learning curriculum (437 topics), a multi-language coding playground (Python, Java, C, C++), curated company interview roadmaps, a community study hub, and an AI-driven resume ATS analyzer into a unified system.

---

## 🚀 Key Platform Features

1. **Interactive Code Playground & Practice Engine:** Multi-language code editor (powered by Monaco Editor) with sandboxed execution, visible and hidden test cases, and memory/time limit bounds.
2. **Curriculum & Knowledge Map:** 437 structured learning topics across DSA, OOP, DBMS, OS, Computer Networks, and System Design with progress tracking.
3. **Company Preparation Roadmaps:** Targeted interview prep paths and patterns for 11+ tech companies.
4. **ATS Resume Analyzer:** Permissive PDF text extraction, section detection, and keyword density feedback.
5. **Community Study Hub:** Real-time peer discussions, study groups, code sharing, and activity feeds.
6. **AI Placement Copilot:** Contextual code explanations and complexity guidance powered by Groq LLM.

---

## 🛠️ Technology Stack

- **Frontend:** Next.js 16 (App Router), React 19, TypeScript, Tailwind CSS v4, Framer Motion, Monaco Editor, Lucide React.
- **Backend:** FastAPI, Python 3.12, Uvicorn, SQLAlchemy 2.0 (async), Alembic, Pydantic v2, PyPDF, Groq.
- **Database:** SQLite (`pathward.db`) with async engine support (`aiosqlite`) and PostgreSQL compatibility.
- **Testing & CI/CD:** PyTest, PyTest-Asyncio, HTTPX, GitHub Actions.

---

## 📖 Quick Setup & Development

Detailed step-by-step instructions for running the frontend and backend locally, executing automated tests, and environment configurations are in the [Setup Guide](./SETUP_GUIDE.md).

```bash
# Backend (Port 8000)
cd backend && python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# Frontend (Port 3000)
cd frontend && npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

```bash
npm run build   # production build
npm run lint    # eslint
```

## Design system

The visual language ("Technical Editorial") is documented in full in
[`DESIGN.md`](./DESIGN.md) at the project root — colors, typography scale,
spacing, elevation levels and component specs. The tokens are implemented as
CSS custom properties in `app/globals.css` and consumed via small utility
classes (`.elevate-1`, `.pill`, `.btn-primary`, `.tag-mono`, etc.) rather than
being duplicated into Tailwind config, so the source of truth stays in one file.

Fonts (Newsreader for display/headings, Geist for UI text, JetBrains Mono for
labels/code) are loaded via a `<link>` tag in `app/layout.tsx` rather than
`next/font/google`, since this sandbox couldn't reach `fonts.googleapis.com`
to verify a build-time font fetch. If you'd rather use `next/font/google`
(recommended for production — self-hosted, no runtime request), swap it in;
it's a five-line change and the font-family names are already correct.

## Project structure

```
app/
  layout.tsx        Root layout, fonts, metadata
  page.tsx           Landing page — assembles all sections
  globals.css        Design tokens + utility classes

components/
  layout/            Navbar, Footer, ScrollProgress
  landing/           One component per landing-page section
  ui/                Reveal/RevealGroup/RevealItem (scroll animation
                      primitives), SectionHeader

lib/data/            Typed content for every section — swap for a real
                      API/database later without touching components
types/                Shared TypeScript interfaces
```

## Sections (all preserved from the original prototype)

1. Hero — scroll-linked parallax, live client-side search over resources/companies
2. Topic strip
3. Learning Paths
4. Placement Roadmap — horizontal stepper + 3-column detail panel (topics /
   resources / practice)
5. Resource Library — filterable card grid
6. Company Preparation — filterable card grid with sample-dated content
7. Practice — featured problem panel + category progress grid
8. Interactive Labs
9. Concept Decoder — tabbed, staged reveal
10. Template Library
11. Knowledge Map — SVG graph, progressive construction on scroll, hover
    tooltips (`components/landing/KnowledgeMap.tsx`)
12. AI Placement Copilot — local mock logic, no API key required
13. Dashboard — count-up score, animated bars, sequential checklist
14. Final CTA + Footer

## Authentication pages

`/login`, `/signup`, `/forgot-password`, `/reset-password`, `/verify-email` — a
split-screen auth flow (shared `BrandPanel` left, form right) using the same
design tokens, fonts and blue accent as the landing page. All are frontend
only right now: forms validate client-side and simulate a network delay, with
no real backend wired up. `Sign in`/`Create account` redirect to `/` and
`/login` respectively after the simulated delay, as placeholders for real
session handling. `components/auth/` holds the shared pieces (`BrandPanel`,
`AuthRightPanel`, `AuthTabs`, `TextField`, `PasswordField`, `GoogleButton`).

## Content

Section copy is **original writing**, structured with the same depth and
information-architecture patterns as the reference brief (12-phase roadmap
with per-stage "frequently tested by" companies, 8 companies with real
round-by-round breakdowns, 4 fully worked CS concepts, a worked 3-Sum
problem with Java solution, 3 AI-copilot role tracks) — not copied verbatim
from any source, per the "final result should be an ORIGINAL platform"
instruction.

## Notes for the next stages

- All content lives in `lib/data/*.ts` as typed arrays/objects — this is the
  seam where a real database (Postgres via an ORM, or a CMS) plugs in without
  touching any component.
- `components/landing/*` are the section components; `components/ui/Reveal.tsx`
  is the reusable animation layer other pages can reuse.
- Company data is explicitly marked as sample/demo with a `verified` date
  field, per the "do not invent current company requirements" instruction —
  wire this to a real, periodically-reviewed source before launch.
- Respects `prefers-reduced-motion` throughout (`useReducedMotion` from
  Framer Motion gates every animated component).
