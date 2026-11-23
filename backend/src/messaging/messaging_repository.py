from typing import Annotated

from fastapi import Depends
from sqlmodel import and_, create_engine, desc, or_, select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.core.config import DATABASE_URL

from ..core.dependencies import get_session
from ..core.models import Messages, Sessions

# create engine
engine = create_engine(DATABASE_URL, echo=True)

SessionDependency = Annotated[AsyncSession, Depends(get_session)]

async def insert_new_message(
        content: str, 
        receiver_id: int, 
        sender_id: int,
        db_session: SessionDependency,
    ):
    message = Messages(receiver_id=receiver_id, sender_id=sender_id, content=content)

    async with db_session:
        db_session.add(message)
        await db_session.commit()


async def get_all_messages(
        sender_id: int, 
        receiver_id: int,
        db_session: SessionDependency,
    ):
    statement = select(Messages).where(
        or_(
            and_(Messages.id == sender_id, Messages.id == receiver_id), 
            and_(Messages.id == receiver_id, Messages.id == sender_id)
        )
    ).order_by(desc(Messages.created_at))
    
    async with db_session:
        result = await db_session.exec(statement)
        return result

async def get_user_id_by_session_id(
        id: str,
        db_session: SessionDependency,
    ) -> int:
    statement = select(Sessions.user_id).where(Sessions.id == id)

    async with db_session:
        result = (await db_session.exec(statement)).one()

    return result