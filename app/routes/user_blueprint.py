from flask import Blueprint
from app.controllers.user_controller import create_user,list_users,get_user,login
from flask_jwt_extended import jwt_required

bp = Blueprint("bp_user",__name__,url_prefix='/api')

bp.post('/user')(create_user)
bp.post('/login')(login)
bp.get('/user')(list_users)
bp.get('/user/<int:id>')(jwt_required()(get_user))