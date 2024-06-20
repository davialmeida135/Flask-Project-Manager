from flask import Blueprint, redirect, render_template, request, url_for, abort
from flask_login import login_required, current_user
from marshmallow import Schema, fields
from app.service.projeto_service import get_projetos_ativos, add_projeto, fetch_projeto as get_projeto, edit_projeto as update_projeto, terminar_projeto, get_projetos_terminados, adicionar_usuario, remover_usuario
from app.service.tarefa_service import fetch_tarefas_projeto as get_tarefas_projeto
from app.service.usuario_service import get_usuarios_projeto, get_usuario_by_username
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
    
    if current_user.id != projeto.idGerente:
        return abort(403)
    
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
    projeto = get_projeto(id)
    if projeto is None:
        return abort(404)
    
    if current_user.id != projeto.idGerente:
        return abort(403)
    
    terminar_projeto(id)
    return redirect(url_for('projeto.listar_projetos'))

@projeto_bp.route("/list/terminados", methods=['GET'])
@login_required
def listar_projetos_terminados():
    projetos_terminados = get_projetos_terminados(current_user.id)
    return render_template("lista_projetos_terminados.html", projetos=projetos_terminados)

@projeto_bp.route("/add-usuario-projeto/<int:idProjeto>", methods=['GET', 'POST'])
@login_required
def add_usuario_projeto_view(idProjeto):
    projeto = get_projeto(idProjeto)
    if projeto is None:
        return abort(404)
    
    if current_user.id != projeto.idGerente:
        return abort(403) 
    
    if request.method == 'GET':
        return render_template("add_usuario_projeto.html", idProjeto=idProjeto)
    
    if request.method == 'POST':
        username = request.form.get('username')
        try:
            usuario = get_usuario_by_username(username)
            if usuario:
                adicionar_usuario(usuario.id, idProjeto)
                return redirect(url_for('projeto.projeto_detalhes', id=idProjeto))
            else:
                error_message = f"Usuário '{username}' não encontrado."
                return render_template("add_usuario_projeto.html", idProjeto=idProjeto, error=error_message)
        except Exception as e:
            error_message = f"Erro ao adicionar usuário ao projeto: {str(e)}"
            return render_template("add_usuario_projeto.html", idProjeto=idProjeto, error=error_message)
        
@projeto_bp.route("/remover-usuario-projeto/<int:idProjeto>", methods=['POST'])
@login_required
def remover_usuario_projeto(idProjeto):
    projeto = get_projeto(idProjeto)
    if projeto is None:
        return abort(404)
    
    if current_user.id != projeto.idGerente:
        return abort(403)

    idUsuario = int(request.form['idUsuario'])
    remover_usuario(idUsuario, idProjeto)
    return redirect(url_for('projeto.projeto_detalhes', id=idProjeto))

