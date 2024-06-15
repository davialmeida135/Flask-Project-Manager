from werkzeug.security import generate_password_hash, check_password_hash
from app.db.usuario import create_usuario, get_usuario_by_username

def register_usuario(nome, username, password):
    hashed_password = generate_password_hash(password)
    create_usuario(nome, username, hashed_password)

def authenticate(username, password):
    user = get_usuario_by_username(username)
    if user and check_password_hash(user.password, password):
        return user
    return None