from . import get_db
from flask_login import UserMixin

def get_all_usuarios():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM Usuario"
    cursor.execute(query)
    usuarios = cursor.fetchall()
    cursor.close()
    return usuarios

def get_usuario_by_id(idUsuario):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM Usuario WHERE idUsuario = %s"
    cursor.execute(query, (idUsuario,))
    usuario = cursor.fetchone()
    cursor.close()
    return usuario

def get_usuario_by_username(username):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    query = """
    SELECT * FROM Usuario
    WHERE username = %s
    """
    cursor.execute(query, (username,))
    usuario = cursor.fetchone()
    cursor.close()
    return usuario if usuario else None

def get_cred(username):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM Credenciais WHERE username = %s"
    cursor.execute(query, (username,))
    cred = cursor.fetchone()
    cursor.close()
    return cred

def create_usuario(nome,username,password):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("START TRANSACTION")
    query = "INSERT INTO Usuario (nome,username) VALUES (%s,%s)"
    cursor.execute(query, (nome,username))
    query = "INSERT INTO Credenciais (username,senha) VALUES (%s,%s)"
    cursor.execute(query, (username,password))
    db.commit()
    idUsuario = cursor.lastrowid
    cursor.close()
    return idUsuario

def update_usuario(id,nome,username):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE Usuario SET nome = %s, username = %s WHERE idUsuario = %s"
    cursor.execute(query, (nome,username,id))
    db.commit()
    cursor.close()

def delete_usuario(idUsuario):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM Usuario WHERE idUsuario = %s"
    cursor.execute(query, (idUsuario,))
    db.commit()
    cursor.close()

def get_usuarios_by_projeto(idProjeto):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    query = """
    SELECT Usuario.*
    FROM Usuario
    JOIN Usuario_Projeto ON Usuario.idUsuario = Usuario_Projeto.idUsuario
    WHERE Usuario_Projeto.idProjeto = %s
    """
    cursor.execute(query, (idProjeto,))
    usuarios = cursor.fetchall()
    cursor.close()
    return usuarios

def get_usuarios_by_tarefa(idTarefa):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    query = """
    SELECT Usuario.*
    FROM Usuario
    JOIN Usuario_Tarefa ON Usuario.idUsuario = Usuario_Tarefa.idUsuario
    WHERE Usuario_Tarefa.idTarefa = %s
    """
    cursor.execute(query, (idTarefa,))
    usuarios = cursor.fetchall()
    cursor.close()
    return usuarios

def change_password(username, password):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE Credenciais SET senha = %s WHERE username = %s"
    cursor.execute(query, (password, username))
    db.commit()
    cursor.close()

