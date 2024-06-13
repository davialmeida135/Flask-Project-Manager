from . import get_db

def get_all_tarefas():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM Tarefa"
    cursor.execute(query)
    tarefas = cursor.fetchall()
    cursor.close()
    return tarefas

def get_tarefa_by_id(idTarefa):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM Tarefa WHERE idTarefa = %s"
    cursor.execute(query, (idTarefa,))
    tarefa = cursor.fetchone()
    cursor.close()
    return tarefa

def create_tarefa(nome, data_criacao, descricao, prazo, status, idProjeto, idUsuarios : list):
    db = get_db()
    cursor = db.cursor()
    query = """
        START TRANSACTION
        INSERT INTO Tarefa (nome, data_criacao, descricao, prazo, status, idProjeto)
        VALUES (%s, %s, %s, %s, %s, %s)
        SET @last_tarefa_id = LAST_INSERT_ID();
        """
    cursor.execute(query, (nome, data_criacao, descricao, prazo, status, idProjeto))

    for idUsuario in idUsuarios:
            query = """
            INSERT INTO Tarefa_Usuario (idUsuario, idTarefa)
            VALUES (%s, @last_tarefa_id)
            """
            cursor.execute(query, (idUsuario,))
    db.commit()
    cursor.close()

def update_tarefa(idTarefa, nome, data_criacao, descricao, prazo, status, idProjeto):
    db = get_db()
    cursor = db.cursor()
    query = """
    UPDATE Tarefa
    SET nome = %s, data_criacao = %s, descricao = %s, prazo = %s, status = %s, idProjeto = %s
    WHERE idTarefa = %s
    """
    cursor.execute(query, (nome, data_criacao, descricao, prazo, status, idProjeto, idTarefa))
    db.commit()
    cursor.close()

def delete_tarefa(idTarefa):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM Tarefa WHERE idTarefa = %s"
    cursor.execute(query, (idTarefa,))
    db.commit()
    cursor.close()

#Todas tarefas do usuario
def get_usuario_tarefas(idUsuario):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM Tarefa WHERE idUsuario = %s"
    cursor.execute(query, (idUsuario,))
    tarefas = cursor.fetchall()
    cursor.close()
    return tarefas

#Tarefas do usuario em um projeto
def get_user_projeto_tarefas(idUsuario, idProjeto):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    query = """SELECT * FROM
                Tarefa NATURAL JOIN Usuario_Tarefa
                WHERE idUsuario = %s
                AND idProjeto = %s"""
    cursor.execute(query, (idUsuario,idProjeto,))
    tarefas = cursor.fetchall()
    cursor.close()
    return tarefas

#Todas tarefas de um projeto
def get_projeto_tarefas(idProjeto):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM Tarefa WHERE idProjeto = %s"
    cursor.execute(query, (idProjeto,))
    tarefas = cursor.fetchall()
    cursor.close()
    return tarefas