# Resume Optimizer — Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        Cloudflare Edge                          │
│               resumeoptimizer.arjism.com (HTTPS)                │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Cloudflare Tunnel (cf-tunnel)                │
│              http://192.168.88.101:8109 (plain HTTP)            │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                        Nginx Reverse Proxy                      │
│                    :8109 → :8000 (backend)                      │
│                    :8110 → :80 (dashboard)                      │
└────────────────────────────┬────────────────────────────────────┘
                             │
              ┌──────────────┴──────────────┐
              ▼                              ▼
┌──────────────────────┐        ┌──────────────────────┐
│   Python + FastAPI   │        │  React Dashboard     │
│   :8000 (internal)   │        │  :80 (internal)      │
│                      │        │                      │
│  - Resume Parsing    │        │  - Tailwind CSS      │
│  - AI Optimization   │        │  - Resume Upload     │
│  - ATS Scoring       │        │  - Score Display     │
│  - PDF Generation    │        │  - Edit Interface    │
└──────────┬───────────┘        └──────────────────────┘
           │
           ▼
┌──────────────────────┐
│   Local Storage      │
│   /app/data/         │
└──────────────────────┘
```

## Tech Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| Language | Python | 3.11+ |
| Web Framework | FastAPI | 0.115+ |
| AI Integration | OpenAI / 9Router | - |
| PDF Processing | PyPDF2, python-docx | - |
| Resume Parsing | Custom + AI | - |
| ATS Analysis | NLP + AI scoring | - |
| Frontend | React + Vite + TypeScript | Vite 5, React 18 |
| Styling | Tailwind CSS | v3 |
| Deployment | Docker Compose | v3.8 |
| Reverse Proxy | Nginx | - |
| Tunnel | Cloudflare Tunnel | - |

## Key Design Decisions

### 1. AI-Powered Analysis
- OpenAI for resume content analysis
- ATS compatibility scoring
- Industry-specific recommendations

### 2. Multi-Format Support
- PDF, DOCX upload and parsing
- Plain text extraction
- Structured data output

### 3. ATS Scoring
- Keyword matching against job descriptions
- Format and structure scoring
- Actionable improvement suggestions

### 4. Privacy-First
- No data stored permanently
- User controls all data
- Secure file handling

## API Endpoints

### Public
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/health` | Health check |

### Authenticated
| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/analyze` | Analyze resume |
| POST | `/api/optimize` | Optimize resume |
| POST | `/api/score` | ATS score |
| GET | `/api/resumes` — List resumes |
| DELETE | `/api/resumes/:id` — Delete resume |

## Ports

| Service | External | Internal |
|---------|----------|----------|
| Backend | `:8109` | `:8000` |
| Dashboard | `:8110` | `:80` |
