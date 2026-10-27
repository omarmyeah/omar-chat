from sqlmodel import Field, SQLModel
from datetime import UTC, datetime

class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str

class Messages(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str
    sender: int = Field(foreign_key="users.id")
    receiver: int = Field(foreign_key="users.id")
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))