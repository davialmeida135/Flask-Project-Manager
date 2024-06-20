from app.db.comentario import (
    get_all_comentarios,
    get_comentario_by_id,
    create_comentario,
    update_comentario,
    delete_comentario,
    get_comentarios_by_tarefa,
    get_feedbacks_by_destinatario_tarefa,
    create_feedback
)
from app.model.comentario import ComentarioModel

def fetch_all_comentarios():
    return get_all_comentarios()

def fetch_comentario_by_id(idComentario):
    return get_comentario_by_id(idComentario)

def fetch_comentario_by_tarefa(idTarefa):
    return get_comentarios_by_tarefa(idTarefa)

def add_comentario(comentario : ComentarioModel):
    if comentario.mensagem != None and comentario.idDestinatario == None:
        return create_comentario(comentario.mensagem, comentario.idUsuario, comentario.idTarefa)
    elif comentario.mensagem != None and comentario.idDestinatario != None:
        return create_feedback(comentario.mensagem, comentario.idUsuario, comentario.idTarefa, comentario.idDestinatario)
    raise ValueError("Comentario não pode ser vazio")
    
def modify_comentario(comentario : ComentarioModel):
    if comentario.mensagem != None:
        return update_comentario(comentario.idComentario, comentario.mensagem, comentario.idUsuario, comentario.idTarefa, comentario.idDestinatario)
    raise ValueError("Comentario não pode ser vazio")
    
def remove_comentario(idComentario):
    delete_comentario(idComentario)

def fetch_feedback_usuario_tarefa(idDestinatario, idTarefa):
    
    return get_feedbacks_by_destinatario_tarefa(idDestinatario, idTarefa)

