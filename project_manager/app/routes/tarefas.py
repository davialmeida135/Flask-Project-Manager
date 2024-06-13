from flask import Blueprint
from flask import (
    abort,
    Blueprint, 
    redirect, 
    request, 
    render_template, 
    url_for
)
from marshmallow import Schema, fields
tarefa_bp = Blueprint('tarefa', __name__)

class TarefaSchema(Schema):
    nome = fields.Str(required=False)
    data_criacao = fields.Date(required=False) #Será definido no codigo
    descricao = fields.Str(required=False)
    prazo = fields.Date(required=False)
    status = fields.Str(required=False) #Opções seletas
    idProjeto = fields.Int(required=False) #Será pré definido
    idUsuarios = fields.String( required=False) #Sera definido na tela



@tarefa_bp.route("/new",methods=['GET', 'POST'])
def create_tarefa():
    if request.method == 'GET':
        
        return render_template("create_tarefa.html")
    if request.method == 'POST':
        tarefa_schema = TarefaSchema()
        tarefa_data = tarefa_schema.load(request.form)
        print(tarefa_data)
        print('oi')
        return render_template("create_tarefa.html")
        