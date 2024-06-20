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

def get_projetos_usuario(idUsuario):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    query = """
    SELECT Projeto.*
    FROM Projeto
    JOIN Usuario_Projeto ON Projeto.idProjeto = Usuario_Projeto.idProjeto
    WHERE Usuario_Projeto.idUsuario = %s
    """
    cursor.execute(query, (idUsuario,))
    projetos = cursor.fetchall()
    cursor.close()
    return projetos

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

def update_projeto(idProjeto,idGerente, data_inicio, nome, descricao, data_fim):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("START TRANSACTION")
    query = """
    UPDATE Projeto
    SET idGerente = %s, data_inicio = %s, nome = %s, descricao = %s, data_fim = %s
    WHERE idProjeto = %s
    """
    cursor.execute(query, (idGerente, data_inicio, nome, descricao, data_fim,idProjeto,))
    db.commit()
    cursor.close()
    

def delete_projeto(idProjeto):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM Projeto WHERE idProjeto = %s"
    cursor.execute(query, (idProjeto,))
    db.commit()
    cursor.close()

def adicionar_usuario_projeto(idUsuario, idProjeto):
    try:
        db = get_db()
        cursor = db.cursor()
        
        query = """
        INSERT INTO Usuario_Projeto (idUsuario, idProjeto)
        VALUES (%s, %s)
        """
        cursor.execute(query, (idUsuario, idProjeto))
        
        db.commit()
        cursor.close()
    except Exception as e:
        raise ValueError(f"Erro ao adicionar usuário ao projeto: {str(e)}")

def remover_usuario_projeto(idUsuario, idProjeto):
    try:
        db = get_db()
        cursor = db.cursor()

        query = """
        DELETE FROM Usuario_Projeto
        WHERE idUsuario = %s AND idProjeto = %s
        """
        cursor.execute(query, (idUsuario, idProjeto))

        db.commit()
        cursor.close()
    except Exception as e:
        raise ValueError(f"Erro ao remover usuário do projeto: {str(e)}")