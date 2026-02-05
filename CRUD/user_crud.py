import re

class NotFound(Exception):
    pass

class AlreadyExist(Exception):
    pass

class WeakPassword(Exception):
    pass


def _validate_password(password: str) -> None:
    if len(password) < 8 or len(password) > 20:
        raise WeakPassword("Password must be 8-20 characters long")

    if not re.search(r"\d", password):
        raise WeakPassword("Password must contain at least one number")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise WeakPassword("Password must contain at least one special character")


def create_user(db, username: str, password: str) -> dict:
    #Create User
    if username in db:
        raise AlreadyExist(f"User '{username}' already exists")

    _validate_password(password)

    user = {"username": username, "password": password}
    db[username] = user
    return user


def read_user(db, username: str) -> dict:
    #Read User
    user = db.get(username)
    if not user:
        raise NotFound(f"User '{username}' not found")
    return user


def update_user(db, username: str, password: str) -> dict:
    #Update User
    user = db.get(username)
    if not user:
        raise NotFound(f"User '{username}' not found")
    
    _validate_password(password)

    user["password"] = password
    db[username] = user
    return user


def delete_user(db, username: str) -> None:
    #Delete User
    if username not in db:
        raise NotFound(f"User '{username}' not found")
    
    del db[username]

def list_users(db) -> list:
    #List Users
    return list(db.values())
def authenticate_user(db, username: str, password: str) -> bool:

    #Authenticate User
    user = db.get(username)
    if not user:
        raise NotFound(f"User '{username}' not found")
    
    return user["password"] == password

