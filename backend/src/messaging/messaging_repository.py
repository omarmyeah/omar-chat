from sqlmodel import Session, and_, create_engine, desc, or_, select

from config import DATABASE_URL

from ..models import Messages, Sessions

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

def get_user_id_by_session_id(id: str) -> int:
    statement = select(Sessions.user_id).where(Sessions.id == id)

    with Session(engine) as session:
        result = session.exec(statement).one()

    return result