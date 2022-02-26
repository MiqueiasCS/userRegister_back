from flask import request,current_app,jsonify
from app.models.user_model import UserModel
from app.utils import check_email,check_user
from app.exceptions import WrongKeysError,InvalidValueError, InvalidEmailError, NotFoundError
from sqlalchemy.exc import IntegrityError



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


def list_users():
    users = UserModel.query.all()
    return jsonify(users)


def get_user(id):
    try:
        user = check_user(id)
        return jsonify(user)
    
    except NotFoundError as err:
        return jsonify(err.message),404