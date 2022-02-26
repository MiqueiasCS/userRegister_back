from app.exceptions import InvalidEmailError
from re import fullmatch
from app.exceptions import NotFoundError
from app.models.user_model import UserModel

def check_email(email: str):
    pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    is_valid = fullmatch(pattern, email)
    if not is_valid:
        raise InvalidEmailError

def check_user(id):
    user = UserModel.query.get(id)
    if not user:
        raise NotFoundError()

    return user