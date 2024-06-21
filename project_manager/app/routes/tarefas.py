from flask import Blueprint, request, render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from app.service.tarefa_service import add_tarefa, remove_tarefa, fetch_tarefa, edit_tarefa
from app.service.comentario_service import fetch_comentario_by_tarefa, fetch_feedback_usuario_tarefa
from marshmallow import Schema, fields
from app.model.tarefa import TarefaModel
from app.model.comentario import ComentarioModel
import datetime

tarefa_bp = Blueprint('tarefa', __name__)

#TODO Definir em uma classe propria, idealmente junto do model 

@tarefa_bp.route('/create/<int:idProjeto>', methods=['GET'])
@login_required
def create_tarefa_view(idProjeto):
    return render_template('create_tarefa.html', idProjeto=idProjeto)
        
@tarefa_bp.route('/create', methods=['POST'])
@login_required
def create_tarefa():
    try:
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        prazo = request.form.get('prazo')
        idUsuarios = request.form.get('idUsuarios')
        idProjeto = request.form.get('idProjeto')

        data_criacao = datetime.date.today()

        status = 'Undone'

        tarefa = TarefaModel(nome=nome, data_criacao=data_criacao, descricao=descricao, prazo=prazo, status=status, idProjeto=idProjeto, idUsuarios=idUsuarios)
        add_tarefa(tarefa)

        return redirect(url_for('projeto.projeto_detalhes', id=idProjeto))
    
    except Exception as e:
        return redirect(url_for('tarefa.create_tarefa_view', idProjeto=idProjeto))
    
@tarefa_bp.route('/delete/<int:idTarefa>/<int:idProjeto>', methods=['GET'])
@login_required
def deletar_tarefa(idTarefa, idProjeto):
    try:
        remove_tarefa(idTarefa)
    except Exception as e:
        print(str(e))
    return redirect(url_for('projeto.projeto_detalhes', id=idProjeto))

@tarefa_bp.route('/details/<int:idTarefa>', methods=['GET'])
@login_required
def tarefa_detalhes(idTarefa):
    tarefa = fetch_tarefa(idTarefa)
    if not tarefa:
        abort(404)
    
    comentarios = fetch_comentario_by_tarefa(idTarefa)
    feedbacks = fetch_feedback_usuario_tarefa(current_user.id, idTarefa)
     
    return render_template('detalhes_tarefa.html', tarefa=tarefa, comentarios=comentarios, feedbacks=feedbacks, idTarefa=idTarefa)

@tarefa_bp.route('/edit/<int:idTarefa>', methods=['GET', 'POST'])
@login_required
def edit_tarefa_view(idTarefa):
    tarefa = fetch_tarefa(idTarefa)
    if not tarefa:
        abort(404)
    
    if request.method == 'POST':
        try:
            nome = request.form.get('nome')
            descricao = request.form.get('descricao')
            prazo = request.form.get('prazo')
            idUsuarios = request.form.get('idUsuarios')
            status = request.form.get('status')

            tarefa.nome = nome
            tarefa.descricao = descricao
            tarefa.prazo = prazo
            tarefa.idUsuarios = idUsuarios
            tarefa.status = status

            edit_tarefa(tarefa)
            return redirect(url_for('tarefa.tarefa_detalhes', idTarefa=idTarefa))
        except Exception as e:
            print(str(e))
    
    return render_template('edit_tarefa.html', tarefa=tarefa)
