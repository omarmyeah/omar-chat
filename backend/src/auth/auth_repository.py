from datetime import datetime

from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from ..core.errors import (
    SessionNotFoundError,
    UserAlreadyExistsError,
    UserNotFoundError,
)
from ..core.models import Sessions, Users


class AuthRepository:
    def __init__(self, session: AsyncSession):
        # internal property do not access
        self._db = session

    async def delete_account(
			self,
            username: str,
            
        ):
        async with self._db:
            statement = select(Users).where(Users.username == username)
            try:
                result = (await self._db.exec(statement)).one()
            except NoResultFound:
                raise UserNotFoundError(username=username)

            await self._db.delete(result)

    async def change_password(
			self,
            username: str, 
            new_password: str,
            
        ):
        async with self._db:
            statement = select(Users).where(Users.username == username)
            try:
                user = (await self._db.exec(statement)).one()
            except NoResultFound:
                raise UserNotFoundError(username=username)

            # change the password of the user being considered
            user.password = new_password

            # add the result to db
            self._db.add(user)

    async def insert_session(
			self,
            session_id: str, 
            csrf_token: str, 
            user_id: int,
            expiration_time: datetime,
            
        ):
        async with self._db:
            session = Sessions(
                id=session_id, 
                user_id=user_id, 
                csrf_token=csrf_token,
                expiration_time=expiration_time,
            )
            self._db.add(session)

    async def get_user_password(
			self,
            username: str,
            
        ):
        # get user password by username
        async with self._db:
            statement = select(Users.password).where(Users.username == username)
            try:
                result = (await self._db.exec(statement)).one()
            except NoResultFound:
                raise UserNotFoundError(username=username)
            
            return result

    async def get_user_id(
			self,
            username: str,
            
        ) -> int:
        # get user id by username
        statement = select(Users.id).where(Users.username == username)

        async with self._db:
            try:
                result = (await self._db.exec(statement)).one()
            except NoResultFound:
                raise UserNotFoundError(username=username)

            if result is None:
                raise UserNotFoundError(username=username)
            
            return result

    async def insert_new_user(
			self,
            username: str, 
            password: str,
            
        ):
        new_user = Users(username=username, password=password)

        async with self._db:
            try:
                self._db.add(new_user)
                await self._db.commit()

                await self._db.refresh(new_user)
                return new_user.id
            except IntegrityError:
                await self._db.rollback()
                raise UserAlreadyExistsError(username=username)

    async def get_csrf_token_by_session_id(
			self,
            id: str,
            
        ) -> str:
        statement = select(Sessions.csrf_token).where(Sessions.id == id)

        async with self._db:
            result = (await self._db.exec(statement)).one()

        return result

    async def delete_session_by_session_id(
			self,
            id: str,
            
        ):
        statement = select(Sessions).where(Sessions.id == id)

        async with self._db:
            # get the result first from db
            result = (await self._db.exec(statement)).first()

            # check if the result doesn't exist before trying to delete.
            if result is None:
                raise SessionNotFoundError(id=id)
            
            await self._db.delete(result)
            await self._db.commit()