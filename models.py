import logging
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
import enum


Base = declarative_base()

class StatusEnum(enum.Enum):
    PROCESSING = "PROCESSING"
    READY = "READY"
    FAILED = "FAILED"

class Downloads(Base):
    __tablename__ = "downloads"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    status = Column(Enum(StatusEnum))
    original_url = Column(String)
    generated_link = Column(String)
    size = Column(Integer, nullable=False, default=0)
    tenant = Column(String, nullable=False)
    ttl = Column(Integer, default=300)
    created_timestamp = Column(DateTime)  # when the file is created completely
    description = Column(String, nullable=True)
    draft_timestamp = Column(DateTime(timezone=True), default=datetime.utcnow)  # When file started processing
    requested_by = Column(String, nullable=False, default="NA")


class DownloadEvents(Base):
    __tablename__ = "download_events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    download_id = Column(ForeignKey("downloads.id", ondelete="CASCADE"))
    user = Column(String)
    ip = Column(String, nullable=False)
    ts = Column(DateTime(timezone=True), default=datetime.utcnow)  # when file is requested

    class Config:
        arbitrary_types_allowed = True