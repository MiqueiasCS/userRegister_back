from app.exceptions import InvalidEmailError
from re import fullmatch
from app.exceptions import NotFoundError,InvalidLoginDataTypeError,WrongKeysError,InvalidValueError
from app.models.user_model import UserModel


def check_create_data(data:dict):
        expected_data = {
            "name":str,
            "email":str,
            "password":str,
            "cep":str,
            "city":str,
            "district":str,
            "street":str,
            "House_number":int
        }
        validated_data = {}
        for key,value_type in expected_data.items():
            item_received = data.get(key)

            if (not item_received):
                raise WrongKeysError(data,expected_data)

            elif (value_type != type(item_received)):
                raise InvalidValueError(data,expected_data)

            else:
                validated_data[key] = item_received
        
        complement = data.get("complement")
        if(complement):
            validated_data["complement"] = complement
        
        return validated_data


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