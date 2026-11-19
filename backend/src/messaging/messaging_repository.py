from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlmodel import Session, and_, create_engine, or_, select, desc

from ..errors import UserAlreadyExistsError, UserNotFoundError
from .models import Messages, Sessions, Users

from config import DATABASE_URL

# create engine
engine = create_engine(DATABASE_URL, echo=True)


def insert_new_message(content: str, receiver_id: int, sender_id: int):
    message = Messages(receiver_id=receiver_id, sender_id=sender_id, content=content)

    with Session(engine) as session:
        session.add(message)
        session.commit()


def get_all_messages(sender_id: int, receiver_id: int):
    statement = select(Messages).where(
        or_(
            and_(Messages.id == sender_id, Messages.id == receiver_id), 
            and_(Messages.id == receiver_id, Messages.id == sender_id)
        )
    ).order_by(desc(Messages.created_at))
    
    with Session(engine) as session:
        result = session.exec(statement)
        return result