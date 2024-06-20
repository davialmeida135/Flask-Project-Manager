from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from marshmallow import Schema, fields
from app.service.projeto_service import get_projetos_ativos, add_projeto, get_projeto, edit_projeto as update_projeto, terminar_projeto, get_projetos_terminados
from app.service.tarefa_service import get_tarefas_projeto
from app.service.usuario_service import get_usuarios_projeto
from app.model.projeto import ProjetoModel
from app.model.tarefa import TarefaModel

projeto_bp = Blueprint('projeto', __name__)

class ProjetoSchema(Schema):
    nome = fields.Str(required=True)
    descricao = fields.Str(required=False)

@projeto_bp.route("/new", methods=['GET', 'POST'])
@login_required
def create_projeto():
    if request.method == 'GET':
        return render_template("create_projeto.html")
    
    if request.method == 'POST':
        projeto_schema = ProjetoSchema()
        projeto_data = projeto_schema.load(request.form)
        
        projeto = ProjetoModel(
            nome=projeto_data['nome'],
            descricao=projeto_data.get('descricao'),
            idGerente=current_user.id,
            idUsuarios=[current_user.id]
        )
        
        add_projeto(projeto)
        return redirect(url_for('projeto.listar_projetos'))

@projeto_bp.route("/list", methods=['GET'])
@login_required
def listar_projetos():
    projetos = get_projetos_ativos(current_user.id)
    return render_template("lista_projetos.html", projetos=projetos)

@projeto_bp.route("/details/<int:id>", methods=['GET'])
def projeto_detalhes(id):
    projeto = get_projeto(id)
    if projeto is None:
        return abort(404)
    tarefas = get_tarefas_projeto(id)
    usuarios = get_usuarios_projeto(id)
    return render_template('projeto_detalhes.html', projeto=projeto, tarefas=tarefas, usuarios=usuarios)


@projeto_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit_projeto_view(id):
    projeto = get_projeto(id)
    if projeto is None:
        return abort(404)
    
    if request.method == 'POST':
        projeto_schema = ProjetoSchema()
        try:
            projeto_data = projeto_schema.load(request.form)
            projeto.nome = projeto_data['nome']
            projeto.descricao = projeto_data.get('descricao')
            update_projeto(projeto)
            return redirect(url_for('projeto.projeto_detalhes', id=projeto.idProjeto))
        except Exception as e:
            print("Erro:", e)
            return render_template("edit_projeto.html", projeto=projeto, error=str(e))
    
    return render_template("edit_projeto.html", projeto=projeto)

@projeto_bp.route("/terminate/<int:id>", methods=['GET'])
def terminar_projeto_view(id):
    print(f'Caiu aqui com id = {id}')
    usuarios = get_usuarios_projeto(id)
    terminar_projeto(id)
    return redirect(url_for('projeto.listar_projetos'))

@projeto_bp.route("/list/terminados", methods=['GET'])
@login_required
def listar_projetos_terminados():
    projetos_terminados = get_projetos_terminados(current_user.id)
    return render_template("lista_projetos_terminados.html", projetos=projetos_terminados)