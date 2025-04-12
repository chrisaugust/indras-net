from pydantic import BaseModel
from datetime import datetime

class DocumentCreate(BaseModel):
    title: str
    original_text: str

class DocumentOut(BaseModel):
    id: int
    title: str
    original_text: str
    summary_text: str | None
    created_at: datetime

    class Config:
        orm_mode = True
