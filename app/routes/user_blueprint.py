from flask import Blueprint
from app.controllers.user_controller import create_user,list_users,get_user

bp = Blueprint("bp_user",__name__,url_prefix='/api')

bp.post('/user')(create_user)
bp.get('/user')(list_users)
bp.get('/user/<int:id>')(get_user)