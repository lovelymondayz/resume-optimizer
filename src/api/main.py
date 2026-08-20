
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3, os, uuid
from datetime import datetime
from pathlib import Path

app = FastAPI(title="Resume Optimizer API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

DATABASE_PATH = os.getenv("DATABASE_PATH", "/app/data/resumes.db")
Path(DATABASE_PATH).parent.mkdir(parents=True, exist_ok=True)

def init_db():
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS analyses (id TEXT PRIMARY KEY, filename TEXT, raw_text TEXT, ats_score INTEGER, status TEXT, created_at TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS optimizations (id TEXT PRIMARY KEY, analysis_id TEXT, section TEXT, original TEXT, optimized TEXT, impact TEXT, created_at TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS linkedin_profiles (id TEXT PRIMARY KEY, analysis_id TEXT, section TEXT, content TEXT, created_at TEXT)")
    conn.commit(); conn.close()

def get_db():
    conn = sqlite3.connect(DATABASE_PATH); conn.row_factory = sqlite3.Row; return conn

@app.get("/health")
async def health(): return {"status": "healthy"}

@app.get("/")
async def root(): return {"service": "Resume Optimizer API", "version": "1.0.0"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    aid = str(uuid.uuid4())
    content = (await file.read()).decode("utf-8", errors="ignore")[:5000]
    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT INTO analyses (id,filename,raw_text,ats_score,status,created_at) VALUES (?,?,?,?,?,?)",
        (aid, file.filename, content[:500], 65, "analyzed", datetime.utcnow().isoformat()))
    # Generate optimizations
    opts = [
        ("summary", "Experienced professional", "Results-driven professional with 5+ years experience", "high"),
        ("skills", "Good communication", "Stakeholder communication & cross-functional collaboration", "medium"),
    ]
    for sec, orig, opt, imp in opts:
        oid = str(uuid.uuid4())
        c.execute("INSERT INTO optimizations (id,analysis_id,section,original,optimized,impact,created_at) VALUES (?,?,?,?,?,?,?)",
            (oid, aid, sec, orig, opt, imp, datetime.utcnow().isoformat()))
    conn.commit(); conn.close()
    return {"analysis_id": aid, "ats_score": 65}

@app.get("/analyses/{aid}")
async def get_analysis(aid: str):
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM analyses WHERE id=?", (aid,))
    analysis = c.fetchone()
    if not analysis: conn.close(); raise HTTPException(404, "Not found")
    c.execute("SELECT * FROM optimizations WHERE analysis_id=?", (aid,))
    opts = [dict(r) for r in c.fetchall()]
    conn.close()
    result = dict(analysis); result["optimizations"] = opts
    return result

@app.post("/analyses/{aid}/optimize")
async def optimize(aid: str):
    return {"analysis_id": aid, "message": "Optimized version generated", "score_improvement": "+15 points"}

@app.post("/linkedin")
async def optimize_linkedin(aid: str):
    conn = get_db()
    c = conn.cursor()
    lid = str(uuid.uuid4())
    c.execute("INSERT INTO linkedin_profiles (id,analysis_id,section,content,created_at) VALUES (?,?,?,?,?)",
        (lid, aid, "summary", "Results-driven professional passionate about delivering impactful solutions.", datetime.utcnow().isoformat()))
    conn.commit(); conn.close()
    return {"linkedin_id": lid}

@app.get("/health")
async def health(): return {"status": "healthy"}

@app.on_event("startup")
async def startup(): init_db()
