from datetime import UTC, datetime

from sqlmodel import Field, SQLModel


class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True)
    password: str


class Messages(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str
    sender_id: int = Field(foreign_key="users.id")
    receiver_id: int = Field(foreign_key="users.id")
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))