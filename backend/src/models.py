from datetime import UTC, datetime, timedelta

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

class Sessions(SQLModel, table=True):
    # the cookie "itself" id
    id: str 

    # the user behind the cookie
    user_id: int = Field(foreign_key="users.id", unique=True)
    
    # the cookie expires certain time after creation
    expiration_time: datetime = Field(default_factory=lambda: datetime.now(UTC) + timedelta(days=30))

    # and finally a csrf token we're doing this kinda manually since this isn't django
    csrf_token: str
    