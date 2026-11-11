from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlmodel import Session, create_engine, select, or_, and_
from ..errors import UserAlreadyExistsError, UserNotFoundError
from .models import Messages, Users, Sessions

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///./{sqlite_file_name}"

# create engine
engine = create_engine(sqlite_url, echo=True)


def get_user_password(username: str):
    # get user password by username
    with Session(engine) as session:
        statement = select(Users.password).where(Users.username == username)
        try:
            result = session.exec(statement).one()
        except NoResultFound:
            raise UserNotFoundError(username=username)
        
        return result


def insert_new_user(username: str, password: str):
    new_user = Users(username=username, password=password)

    with Session(engine) as session:
        try:
            session.add(new_user)
            session.commit()

            return session.refresh().id
        except IntegrityError:
            session.rollback()
            raise UserAlreadyExistsError(username=username)


def insert_new_message(content: str, receiver_id: int, sender_id: int):
    message = Messages(receiver=receiver_id, sender=sender_id, content=content)

    with Session(engine) as session:
        session.add(message)
        session.commit()


def get_all_messages(sender_id: int, receiver_id: int):
    statement = select(Messages).where(
        or_(
            and_(Messages.id == sender_id, Messages.id == receiver_id), 
            and_(Messages.id == receiver_id, Messages.id == sender_id)
        )
    ).order_by(Messages.created_at.desc())
    
    with Session(engine) as session:
        result = session.exec(statement)
        return result

def delete_account(username: str):
    with Session(engine) as session:
        statement = session.select(Users).where(Users.username == username)
        try:
            result = session.exec(statement).one()
        except NoResultFound:
            raise UserNotFoundError(username=username)

        session.delete(result)

def change_password(username: str, new_password: str):
    with Session(engine) as session:
        statement = session.select(Users).where(Users.username == username)
        try:
            user = session.exec(statement).one()()
        except NoResultFound:
            raise UserNotFoundError(username=username)

        # change the password of the user being considered
        user.password = new_password

        # add the result to db
        session.add(user)

def insert_session(session_id: str, user_id: int):
    with Session(engine) as sqlmodel_session:
        # to avoid name conflict between session and sqlmodel 
        session = Sessions(id=session_id, user_id=user_id)