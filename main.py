from fastapi import FastAPI
from app.api.v1.endpoints import analyze
from app.core.database import engine, Base

app = FastAPI(title="Indra's Net")

# Create tables on startup
Base.metadata.create_all(bind=engine)

# Include router
app.include_router(analyze.router, prefix="/api/v1/analyze", tags=["analyze"])
