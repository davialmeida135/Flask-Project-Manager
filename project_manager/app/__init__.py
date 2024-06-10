from flask import Flask 
from flask_login import LoginManager, login_user
from .db import init_app
from .routes import main

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config.from_prefixed_env()

    init_app(app)
    login_manager.init_app(app)
    app.register_blueprint(main)

    from app.home import bp as home_bp
    app.register_blueprint(home_bp)

    from app.projeto import bp as projeto_bp
    app.register_blueprint(projeto_bp, url_prefix='/projetos')

    return app

'''
@login_manager.user_loader
def load_user(user_id):
    from app.db.usuario import get_usuario_by_id
    return get_usuario_by_id(user_id)
'''
