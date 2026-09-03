# Resume Optimizer — AI Resume Analysis

An AI-powered resume optimization tool that analyzes resumes, scores ATS compatibility, and provides improvement recommendations.

## Quick Start

```bash
# Clone
git clone https://github.com/lovelymondayz/resume-optimizer.git
cd resume-optimizer

# Start all services
docker compose up -d --build

# Dashboard: http://localhost:8110
# API: http://localhost:8109
```

## Features

- **Resume Parsing**: PDF and DOCX support with structured extraction
- **ATS Scoring**: See how your resume scores against applicant tracking systems
- **AI Recommendations**: Get personalized improvement suggestions
- **Cover Letter Generation**: AI-generated cover letters based on your resume
- **Privacy-First**: Your resume data is never stored permanently

## API Endpoints

### Public
- `GET /api/health` — Health check

### Authenticated
- `POST /api/analyze` — Analyze resume
- `POST /api/optimize` — Optimize resume
- `POST /api/score` — ATS score
- `GET /api/resumes` — List resumes
- `DELETE /api/resumes/:id` — Delete resume

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| OPENAI_API_KEY | - | OpenAI API key |
| DATABASE_PATH | /app/data | Data directory |
| OUTPUT_DIR | - | Output directory |
| API_KEY | - | Tenant API key |

## Development

```bash
# Backend only
cd backend
pip install -r requirements.txt
uvicorn src.api:app --reload

# Frontend only
cd frontend
npm install
npm run dev
```

## Deployment

1. Push to `main` → GitHub Action auto-deploys
2. Or manually: `ssh vps && cd /root/resume-optimizer && ./update.sh`

## License

MIT
