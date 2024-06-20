from . import get_db

def get_all_comentarios():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM Comentario"
    cursor.execute(query)
    comentarios = cursor.fetchall()
    cursor.close()
    return comentarios

def get_comentario_by_id(idComentario):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM Comentario WHERE idComentario = %s"
    cursor.execute(query, (idComentario,))
    comentario = cursor.fetchone()
    cursor.close()
    return comentario

def get_comentarios_by_tarefa(idTarefa):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM Comentario WHERE idTarefa = %s AND idDestinatario IS NULL"
    cursor.execute(query, (idTarefa,))
    comentarios = cursor.fetchall()
    cursor.close()
    return comentarios

def create_comentario(mensagem, idUsuario, idTarefa):
    db = get_db()
    cursor = db.cursor()
    query = """
    INSERT INTO Comentario (mensagem, idUsuario, idTarefa)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (mensagem, idUsuario, idTarefa))
    db.commit()
    idComentario = cursor.lastrowid
    cursor.close()
    return idComentario

def update_comentario(idComentario, mensagem, idUsuario, idTarefa, idDestinatario=None):
    db = get_db()
    cursor = db.cursor()
    query = """
    UPDATE Comentario
    SET mensagem = %s, idUsuario = %s, idTarefa = %s, idDestinatario = %s
    WHERE idComentario = %s
    """
    cursor.execute(query, (mensagem, idUsuario, idTarefa, idDestinatario, idComentario))
    db.commit()
    cursor.close()

def delete_comentario(idComentario):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM Comentario WHERE idComentario = %s"
    cursor.execute(query, (idComentario,))
    db.commit()
    cursor.close()

def create_feedback(mensagem, idUsuario, idTarefa, idDestinatario):
    db = get_db()
    cursor = db.cursor()
    query = """
    INSERT INTO Comentario (mensagem, idUsuario, idTarefa, idDestinatario)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (mensagem, idUsuario, idTarefa, idDestinatario))
    db.commit()
    idComentario = cursor.lastrowid
    cursor.close()
    return idComentario

def get_feedbacks_by_destinatario_tarefa(idDestinatario, idTarefa):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM Comentario WHERE idDestinatario = %s AND idTarefa = %s"
    cursor.execute(query, (idDestinatario, idTarefa))
    comentarios = cursor.fetchall()
    cursor.close()
    return comentarios