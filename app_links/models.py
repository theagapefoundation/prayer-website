from typing import Optional
import uuid
from datetime import datetime

from sqlmodel import Field, SQLModel


# Create your models here.
class Content(SQLModel, table=True):
    __tablename__ = "contents"

    id: Optional[int] = Field(primary_key=True)
    user_id: str
    created_at: datetime
    path: str
    alt: Optional[str]
    processed: bool


class Group(SQLModel, table=True):
    __tablename__ = "groups"

    id: Optional[uuid.UUID] = Field(primary_key=True)
    name: str
    description: str
    admin_id: str
    banner: int = Field(foreign_key="contents.id", alias="banner_id")
    membership_type: str
    updated_at: datetime
    created_at: datetime
