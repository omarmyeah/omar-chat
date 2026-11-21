from datetime import datetime

from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlmodel import Session, create_engine, select

from config import DATABASE_URL

from ..errors import (
    UserAlreadyExistsError, 
    UserNotFoundError, 
    SessionNotFoundError,
)
from ..models import Sessions, Users

# create engine
engine = create_engine(DATABASE_URL, echo=True)

def delete_account(username: str):
    with Session(engine) as session:
        statement = select(Users).where(Users.username == username)
        try:
            result = session.exec(statement).one()
        except NoResultFound:
            raise UserNotFoundError(username=username)

        session.delete(result)

def change_password(username: str, new_password: str):
    with Session(engine) as session:
        statement = select(Users).where(Users.username == username)
        try:
            user = session.exec(statement).one()()
        except NoResultFound:
            raise UserNotFoundError(username=username)

        # change the password of the user being considered
        user.password = new_password

        # add the result to db
        session.add(user)

def insert_session(
        session_id: str, 
        csrf_token: str, 
        user_id: int,
        expiration_time: datetime,
    ):
    with Session(engine) as sqlmodel_session:
        # to avoid name conflict between session and sqlmodel 
        session = Sessions(
            id=session_id, 
            user_id=user_id, 
            csrf_token=csrf_token,
            expiration_time=expiration_time,
        )
        sqlmodel_session.add(session)

def get_user_password(username: str):
    # get user password by username
    with Session(engine) as session:
        statement = select(Users.password).where(Users.username == username)
        try:
            result = session.exec(statement).one()
        except NoResultFound:
            raise UserNotFoundError(username=username)
        
        return result

def get_user_id(username: str) -> int:
    # get user id by username
    statement = select(Users.id).where(Users.username == username)

    with Session(engine) as session:
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

            session.refresh(new_user)
            return new_user.id
        except IntegrityError:
            session.rollback()
            raise UserAlreadyExistsError(username=username)

def get_csrf_token_by_session_id(id: str) -> str:
    statement = select(Sessions.csrf_token).where(Sessions.id == id)

    with Session(engine) as session:
        result = session.exec(statement).one()

    return result

def delete_session_by_session_id(id: str):
    statement = select(Sessions).where(Sessions.id == id)

    with Session(engine) as session:
        # get the result first from db
        result = session.exec(statement).first()

        # check if the result doesn't exist before trying to delete.
        if result is None:
            raise SessionNotFoundError
        
        session.delete(result)
        session.commit()