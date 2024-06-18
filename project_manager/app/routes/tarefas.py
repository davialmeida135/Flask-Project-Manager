from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.service.tarefa_service import add_tarefa, remove_tarefa
from marshmallow import Schema, fields
from app.model.tarefa import TarefaModel
import datetime

tarefa_bp = Blueprint('tarefa', __name__)

#TODO Definir em uma classe propria, idealmente junto do model
class TarefaSchema(Schema):
    nome = fields.Str(required=False)
    data_criacao = fields.Date(required=False)
    descricao = fields.Str(required=False)
    prazo = fields.Date(required=False)
    status = fields.Str(required=False)
    idProjeto = fields.Int(required=False)
    idUsuarios = fields.String( required=False) 

@tarefa_bp.route('/create/<int:idProjeto>', methods=['GET'])
def create_tarefa_view(idProjeto):
    return render_template('create_tarefa.html', idProjeto=idProjeto)
        
@tarefa_bp.route('/create', methods=['POST'])
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
def deletar_tarefa(idTarefa, idProjeto):
    try:
        remove_tarefa(idTarefa)
    except Exception as e:
        print(str(e))
    return redirect(url_for('projeto.projeto_detalhes', id=idProjeto))