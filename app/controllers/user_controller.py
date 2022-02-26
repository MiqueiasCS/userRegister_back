from flask import request,current_app,jsonify
from app.models.user_model import UserModel
from app.utils import check_email,check_user,check_login_data
from app.exceptions import EmailNotFoundError, IncorrectPasswordError, WrongKeysError,InvalidValueError, InvalidEmailError, NotFoundError,InvalidLoginDataTypeError
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token


def  create_user():
    session = current_app.db.session

    body = request.get_json()
    try:
        data = UserModel.check_data(body)
        check_email(data["email"])

        password_to_hash = data.pop("password")

        user = UserModel(**data)
        user.password = password_to_hash
        
        session.add(user)
        session.commit()

        return jsonify(user),201
    except WrongKeysError as err:
        return jsonify(err.message),400
    except InvalidValueError as err:
        return jsonify(err.message),400
    except InvalidEmailError as err:
        return jsonify(err.message),400
    except IntegrityError:
        return jsonify({"message":"email already exists"}),409

def login():
    body = request.get_json()
    try:
        email,password = check_login_data(body)
        
        user:UserModel = UserModel.query.filter_by(email=email).first()

        if not user:
            raise EmailNotFoundError(email)
    
        if not user.check_password(password):
            raise IncorrectPasswordError()
    
        access_token = create_access_token({"id":user.id,"email":user.email})
        
        return jsonify({"acess_token":access_token}),200
    except InvalidLoginDataTypeError as err:
        return jsonify(err.message),400    
    except EmailNotFoundError as err:
        return jsonify(err.message),404
    except IncorrectPasswordError as err:
        return jsonify(err.message),401


def list_users():
    users = UserModel.query.all()
    return jsonify(users),200


def get_user(id):
    try:
        user = check_user(id)
        return jsonify(user),200
    
    except NotFoundError as err:
        return jsonify(err.message),404
