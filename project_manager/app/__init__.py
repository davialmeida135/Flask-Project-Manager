from flask import Flask 
from flask_login import LoginManager, login_user
from .db import init_app
import os
import secrets
login_manager = LoginManager()
login_manager.login_view = "auth.login"

def create_app():
    app = Flask(__name__)

    app.secret_key = secrets.token_hex(16)
    app.config.from_prefixed_env()

    init_app(app)
    login_manager.init_app(app)
    
    from .rotas import main
    app.register_blueprint(main)
    from .routes.tarefas import tarefa_bp
    from .routes.projetos import projeto_bp
    app.register_blueprint(tarefa_bp, url_prefix='/tarefas')
    app.register_blueprint(projeto_bp, url_prefix='/projetos')

    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    from .routes.home import home_bp
    app.register_blueprint(home_bp, url_prefix='/home')

    return app


@login_manager.user_loader
def load_user(user_id):
    from app.service.usuario_service import get_usuario_by_id
    return get_usuario_by_id(user_id)

