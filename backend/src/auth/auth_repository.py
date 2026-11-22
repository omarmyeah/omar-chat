from datetime import datetime

from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import Session, create_engine, select

from ..core.errors import (
    UserAlreadyExistsError, 
    UserNotFoundError, 
    SessionNotFoundError,
)
from ..core.models import Sessions, Users
from ..core.dependencies import get_session
from fastapi import Depends
from typing import Annotated

SessionDependency = Annotated[AsyncSession, Depends(get_session)]

def delete_account(
        username: str,
        db_session: SessionDependency,
    ):
    with db_session:
        statement = select(Users).where(Users.username == username)
        try:
            result = db_session.exec(statement).one()
        except NoResultFound:
            raise UserNotFoundError(username=username)

        db_session.delete(result)

def change_password(
        username: str, 
        new_password: str,
        db_session: SessionDependency,
    ):
    with db_session:
        statement = select(Users).where(Users.username == username)
        try:
            user = db_session.exec(statement).one()()
        except NoResultFound:
            raise UserNotFoundError(username=username)

        # change the password of the user being considered
        user.password = new_password

        # add the result to db
        db_session.add(user)

def insert_session(
        session_id: str, 
        csrf_token: str, 
        user_id: int,
        expiration_time: datetime,
        db_session: SessionDependency,
    ):
    with db_session:
        session = Sessions(
            id=session_id, 
            user_id=user_id, 
            csrf_token=csrf_token,
            expiration_time=expiration_time,
        )
        db_session.add(session)

def get_user_password(
        username: str,
        db_session: SessionDependency,
    ):
    # get user password by username
    with db_session:
        statement = select(Users.password).where(Users.username == username)
        try:
            result = db_session.exec(statement).one()
        except NoResultFound:
            raise UserNotFoundError(username=username)
        
        return result

def get_user_id(
        username: str,
        db_session: SessionDependency,
    ) -> int:
    # get user id by username
    statement = select(Users.id).where(Users.username == username)

    with db_session:
        try:
            result = db_session.exec(statement).one()
        except NoResultFound:
            raise UserNotFoundError(username=username)
        
        return result

def insert_new_user(
        username: str, 
        password: str,
        db_session: SessionDependency,
    ):
    new_user = Users(username=username, password=password)

    with db_session:
        try:
            db_session.add(new_user)
            db_session.commit()

            db_session.refresh(new_user)
            return new_user.id
        except IntegrityError:
            db_session.rollback()
            raise UserAlreadyExistsError(username=username)

def get_csrf_token_by_session_id(
        id: str,
        db_session: SessionDependency,
    ) -> str:
    statement = select(Sessions.csrf_token).where(Sessions.id == id)

    with db_session:
        result = db_session.exec(statement).one()

    return result

def delete_session_by_session_id(
        id: str,
        db_session: SessionDependency,
    ):
    statement = select(Sessions).where(Sessions.id == id)

    with db_session:
        # get the result first from db
        result = db_session.exec(statement).first()

        # check if the result doesn't exist before trying to delete.
        if result is None:
            raise SessionNotFoundError
        
        db_session.delete(result)
        db_session.commit()