from datetime import datetime
from typing import Annotated

from fastapi import Depends
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from ..core.dependencies import get_session
from ..core.errors import (
    SessionNotFoundError,
    UserAlreadyExistsError,
    UserNotFoundError,
)
from ..core.models import Sessions, Users

SessionDependency = Annotated[AsyncSession, Depends(get_session)]

async def delete_account(
        username: str,
        db_session: SessionDependency,
    ):
    async with db_session:
        statement = select(Users).where(Users.username == username)
        try:
            result = (await db_session.exec(statement).one())
        except NoResultFound:
            raise UserNotFoundError(username=username)

        await db_session.delete(result)

async def change_password(
        username: str, 
        new_password: str,
        db_session: SessionDependency,
    ):
    async with db_session:
        statement = select(Users).where(Users.username == username)
        try:
            user = await db_session.exec(statement).one()()
        except NoResultFound:
            raise UserNotFoundError(username=username)

        # change the password of the user being considered
        user.password = new_password

        # add the result to db
        await db_session.add(user)

async def insert_session(
        session_id: str, 
        csrf_token: str, 
        user_id: int,
        expiration_time: datetime,
        db_session: SessionDependency,
    ):
    async with db_session:
        session = Sessions(
            id=session_id, 
            user_id=user_id, 
            csrf_token=csrf_token,
            expiration_time=expiration_time,
        )
        await db_session.add(session)

async def get_user_password(
        username: str,
        db_session: SessionDependency,
    ):
    # get user password by username
    async with db_session:
        statement = select(Users.password).where(Users.username == username)
        try:
            result = await db_session.exec(statement).one()
        except NoResultFound:
            raise UserNotFoundError(username=username)
        
        return result

async def get_user_id(
        username: str,
        db_session: SessionDependency,
    ) -> int:
    # get user id by username
    statement = select(Users.id).where(Users.username == username)

    async with db_session:
        try:
            result = await db_session.exec(statement).one()
        except NoResultFound:
            raise UserNotFoundError(username=username)
        
        return result

async def insert_new_user(
        username: str, 
        password: str,
        db_session: SessionDependency,
    ):
    new_user = Users(username=username, password=password)

    async with db_session:
        try:
            await db_session.add(new_user)
            await db_session.commit()

            await db_session.refresh(new_user)
            return new_user.id
        except IntegrityError:
            await db_session.rollback()
            raise UserAlreadyExistsError(username=username)

async def get_csrf_token_by_session_id(
        id: str,
        db_session: SessionDependency,
    ) -> str:
    statement = select(Sessions.csrf_token).where(Sessions.id == id)

    async with db_session:
        result = await db_session.exec(statement).one()

    return result

async def delete_session_by_session_id(
        id: str,
        db_session: SessionDependency,
    ):
    statement = select(Sessions).where(Sessions.id == id)

    async with db_session:
        # get the result first from db
        result = await db_session.exec(statement).first()

        # check if the result doesn't exist before trying to delete.
        if result is None:
            raise SessionNotFoundError
        
        await db_session.delete(result)
        await db_session.commit()