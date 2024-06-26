from werkzeug.security import generate_password_hash, check_password_hash
import app.db.usuario as db_usuario
from app.model.usuario import UsuarioModel

def register_usuario(usuario):
    if (usuario['password'] != usuario['confirm_password']):
        raise ValueError("Passwords do not match")
    
    if len(usuario['username'])<4:
        raise ValueError("Username must be at least 4 characters")
    if len(usuario['password'])<6:
        raise ValueError("Password must be at least 6 characters")
    
    if len(usuario['username']) > 45:  # Assuming the column limit is 45 characters
        raise ValueError("Username must be at maximum 45 characters")
    
    hashed_password = generate_password_hash(usuario['password'])
    try:
        db_usuario.create_usuario(usuario['nome'], usuario['username'], hashed_password)
    except Exception as e:
        raise ValueError("Could not create user: " + str(e))

def authenticate(username, password):
    cred = get_cred(username)
    if cred and check_password_hash(cred['senha'], password):
        return get_usuario_by_username(username)
    raise ValueError("Could not authenticate user")

def get_usuario_by_username(username):
    temp = db_usuario.get_usuario_by_username(username)
    if temp:
        return UsuarioModel(temp["idUsuario"], temp["nome"], temp["username"])
        
    else:
        raise ValueError("User not found")
    
def get_cred(username):
    temp = db_usuario.get_cred(username)
    if temp:
        return temp
    else:
        raise ValueError("User not found")
    
def get_usuario_by_id(idUsuario):
    temp = db_usuario.get_usuario_by_id(idUsuario)
    if temp:
        return UsuarioModel(temp["idUsuario"], temp["nome"], temp["username"])
    else:
        raise ValueError("User not found")

def get_usuarios_projeto(id):
    usuarios_data = db_usuario.get_usuarios_by_projeto(id)
    usuarios = [UsuarioModel(id=usuario['idUsuario'], nome=usuario['nome'], username=usuario['username']) for usuario in usuarios_data]
    return usuarios

