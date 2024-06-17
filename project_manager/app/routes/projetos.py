from flask import Blueprint, redirect, render_template, request, url_for
from marshmallow import Schema, fields
from app.service.projeto_service import get_projetos, add_projeto
from app.model.projeto import ProjetoModel

projeto_bp = Blueprint('projeto', __name__)

class ProjetoSchema(Schema):
    nome = fields.Str(required=True)
    descricao = fields.Str(required=False)
    data_inicio = fields.Date(required=False)
    data_fim = fields.Date(required=False)
    idGerente = fields.Int(required=True)

@projeto_bp.route("/new", methods=['GET', 'POST'])
def create_projeto():
    if request.method == 'GET':
        return render_template("create_projeto.html")
    if request.method == 'POST':
        projeto_schema = ProjetoSchema()
        projeto_data = projeto_schema.load(request.form)
        projeto = ProjetoModel(
            nome=projeto_data['nome'],
            descricao=projeto_data.get('descricao'),
            data_inicio=projeto_data.get('data_inicio'),
            data_fim=projeto_data.get('data_fim'),
            idGerente=projeto_data['idGerente'],
            idUsuarios=[]
        )
        add_projeto(projeto)
        return redirect(url_for('projeto.listar_projetos'))

@projeto_bp.route("/list", methods=['GET'])
def listar_projetos():
    projetos = get_projetos()
    return render_template("lista_projetos.html", projetos=projetos)