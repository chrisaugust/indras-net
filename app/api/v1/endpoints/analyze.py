from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.document import DocumentCreate, DocumentOut
from app.models.document import Document
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DocumentOut)
def analyze_document(doc: DocumentCreate, db: Session = Depends(get_db)):
    new_doc = Document(
        title=doc.title,
        original_text=doc.original_text,
        summary_text=None, # here's where we'll make the OpenAI call
    )
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc
