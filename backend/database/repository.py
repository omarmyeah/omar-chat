from sqlmodel import Session, create_engine, select
from .models import Users, Messages
from ..schemas import User

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///./{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def get_user_password(username: str):
    with Session(engine) as session:
        statement = select(Users.password).where(Users.username == username)
        result = session.exec(statement).first()

        return result

def insert_new_user(user: User):
    row = Users(username=user.username, password=user.password)

    with Session(engine) as session:
        session.add(row)

def insert_new_message(receiver_id: int, sender_id: int, content: str):
    message = Messages(receiver=receiver_id, sender=sender_id, content=content)
    
    with Session(engine) as session:
        session.add(message)