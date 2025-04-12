from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    original_text = Column(Text)
    summary_text = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
