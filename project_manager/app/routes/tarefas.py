from flask import Blueprint

tarefa_bp = Blueprint('tarefa', __name__)
from marshmallow import Schema, fields

class TarefaSchema(Schema):
    nome = fields.Str(required=True)
    data_criacao = fields.Date(required=True)
    descricao = fields.Str(required=True)
    prazo = fields.Date(required=True)
    status = fields.Str(required=True)
    idProjeto = fields.Int(required=True)
    idUsuarios = fields.List(fields.Int(), required=True)

from flask import (
    abort,
    Blueprint, 
    redirect, 
    request, 
    render_template, 
    url_for
)

@tarefa_bp.route("/new",methods=['GET', 'POST'])
def create_tarefa():
    if request.method == 'GET':
        return render_template("create_tarefa.html")
    if request.method == 'POST':
        
        print('oi')
        return render_template("single.html")
        