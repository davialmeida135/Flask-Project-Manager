from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.service.tarefa_service import add_tarefa
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
        # Receber os dados do formulário
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        prazo = request.form.get('prazo')
        idUsuarios = request.form.get('idUsuarios')
        idProjeto = request.form.get('idProjeto')

        # Definir data de criação como a data atual
        data_criacao = datetime.date.today()

        # Definir status padrão como 'Undone'
        status = 'Undone'

        # Criar a tarefa usando o serviço
        tarefa = TarefaModel(nome=nome, data_criacao=data_criacao, descricao=descricao, prazo=prazo, status=status, idProjeto=idProjeto, idUsuarios=idUsuarios)
        add_tarefa(tarefa)

        return redirect(url_for('projeto.projeto_detalhes', id=idProjeto))
    
    except Exception as e:
        return redirect(url_for('tarefa.create_tarefa_view', idProjeto=idProjeto))