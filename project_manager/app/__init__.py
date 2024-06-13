from flask import Flask 
from flask_login import LoginManager, login_user
from .db import init_app



login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config.from_prefixed_env()

    init_app(app)
    login_manager.init_app(app)
    
    from .rotas import main
    app.register_blueprint(main)
    from .routes.tarefas import tarefa_bp
    app.register_blueprint(tarefa_bp, url_prefix='/tarefas')




    return app


@login_manager.user_loader
def load_user(user_id):
    from app.db.usuario import get_usuario_by_id
    return get_usuario_by_id(user_id)

