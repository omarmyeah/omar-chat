class UserAlreadyExistsError(Exception):
    def __int__(self, username: str):
        self.username = username
        super().__init__(f"The username {username} is already taken.")

class UserNotFoundError(Exception):
    def __init__(self, username):
        super().__init__(f"The user with username {username} doesn't exist.")