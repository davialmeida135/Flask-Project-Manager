from app.db.comentario import (
    get_all_comentarios,
    get_comentario_by_id as db_get_comentario_by_id,
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
    data = db_get_comentario_by_id(idComentario)
    if data:
        return ComentarioModel(
            idComentario=data['idComentario'],
            mensagem=data['mensagem'],
            idUsuario=data['idUsuario'],
            idTarefa=data['idTarefa'],
            idDestinatario=data.get('idDestinatario')
        )
    return None

def fetch_comentario_by_tarefa(idTarefa):
    return get_comentarios_by_tarefa(idTarefa)

def add_comentario(comentario: ComentarioModel):
    if comentario.mensagem is not None and comentario.idDestinatario is None:
        return create_comentario(comentario.mensagem, comentario.idUsuario, comentario.idTarefa)
    elif comentario.mensagem is not None and comentario.idDestinatario is not None:
        return create_feedback(comentario.mensagem, comentario.idUsuario, comentario.idTarefa, comentario.idDestinatario)
    raise ValueError("Comentario não pode ser vazio")

def modify_comentario(comentario: ComentarioModel):
    if comentario.mensagem is not None:
        return update_comentario(comentario.idComentario, comentario.mensagem, comentario.idUsuario, comentario.idTarefa, comentario.idDestinatario)
    raise ValueError("Comentario não pode ser vazio")

def remove_comentario(idComentario):
    delete_comentario(idComentario)

def fetch_feedback_usuario_tarefa(idDestinatario, idTarefa):
    return get_feedbacks_by_destinatario_tarefa(idDestinatario, idTarefa)