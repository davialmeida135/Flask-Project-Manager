from flask import Blueprint, request, render_template, redirect, url_for, abort
from flask_login import login_required, current_user
from app.service.comentario_service import add_comentario, fetch_comentario_by_tarefa, fetch_feedback_usuario_tarefa
from app.service.usuario_service import get_usuario_by_username
from app.model.comentario import ComentarioModel

comentario_bp = Blueprint('comentario', __name__)

@comentario_bp.route('/create/<int:idTarefa>', methods=['GET'])
@login_required
def create_comentario_view(idTarefa):
    return render_template('create_comentario.html', idTarefa=idTarefa)

@comentario_bp.route('/create', methods=['POST'])
@login_required
def create_comentario():
    try:
        mensagem = request.form.get('mensagem')
        idUsuario = current_user.id
        idTarefa = request.form.get('idTarefa')
        usernameDestinatario = request.form.get('usernameDestinatario')

        if not mensagem:
            return redirect(url_for('comentario.create_comentario_view', idTarefa=idTarefa))

        # Busca o ID do destinatário pelo username, se fornecido
        idDestinatario = None
        if usernameDestinatario:
            destinatario = get_usuario_by_username(usernameDestinatario)
            idDestinatario = destinatario.id if destinatario else None

        comentario = ComentarioModel(mensagem=mensagem, idUsuario=idUsuario, idTarefa=idTarefa, idDestinatario=idDestinatario)
        add_comentario(comentario)

        return redirect(url_for('tarefa.tarefa_detalhes', idTarefa=idTarefa))

    except Exception as e:
        print('Ocorreu um erro ao adicionar o comentário', e)
        return redirect(url_for('comentario.create_comentario_view', idTarefa=idTarefa))