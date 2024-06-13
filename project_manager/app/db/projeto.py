from . import get_db

def get_all_projetos():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM Projeto"
    cursor.execute(query)
    projetos = cursor.fetchall()
    cursor.close()
    return projetos

def get_projeto_by_id(idProjeto):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM Projeto WHERE idProjeto = %s"
    cursor.execute(query, (idProjeto,))
    projeto = cursor.fetchone()
    cursor.close()
    return projeto

def create_projeto(idGerente, data_inicio, nome, descricao, data_fim, usuarios: list):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("START TRANSACTION")
    query = """
    INSERT INTO Projeto (idGerente, data_inicio, nome, descricao, data_fim)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (idGerente, data_inicio, nome, descricao, data_fim))
    cursor.execute("SET @last_projeto_id = LAST_INSERT_ID()")
    for usuario in usuarios:
        query = """
        INSERT INTO Usuario_Projeto (idUsuario, idProjeto)
        VALUES (%s, @last_projeto_id)
            """
        cursor.execute(query, (usuario,))
    
    db.commit()
    idProjeto = cursor.lastrowid
    cursor.close()
    
    return idProjeto

#TODO
def update_projeto(projeto):
    db = get_db()
    cursor = db.cursor()
    query = """
    UPDATE Projeto
    SET idGerente = %s, data_inicio = %s, nome = %s, descricao = %s, data_fim = %s
    WHERE idProjeto = %s
    """
    cursor.execute(query, (projeto.idGerente, projeto.data_inicio, projeto.nome, projeto.descricao, projeto.data_fim, projeto.idProjeto))
    db.commit()
    cursor.close()

def delete_projeto(idProjeto):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM Projeto WHERE idProjeto = %s"
    cursor.execute(query, (idProjeto,))
    db.commit()
    cursor.close()