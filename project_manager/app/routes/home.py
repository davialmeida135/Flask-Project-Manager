from flask import Blueprint, render_template
from flask_login import current_user
from app.model.usuario import UsuarioModel

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    # Check if user is logged in
    try:
        user_info = {
            'name': current_user.nome,
            'username': current_user.username,
            'id': current_user.id
        }
    except:
        # Set default user info if user is not logged in
        user_info = {
            'name': 'Guest',
            'email': '',
            'age': 0
        }
        

    return render_template('home.html', user_info=user_info)