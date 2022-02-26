from app.exceptions import InvalidEmailError
from re import fullmatch
from app.exceptions import NotFoundError,InvalidLoginDataTypeError
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

def check_login_data(body):
    email = body.get('email')
    password = body.get('password')
        
    if(not email or not password):
        raise InvalidLoginDataTypeError("you must pass a valid email and password")

    if (type(email) != str or type(password) != str):
        raise InvalidLoginDataTypeError("The email and password must be of type string")
    
    return email,password 