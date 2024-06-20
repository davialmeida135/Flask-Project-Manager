from flask import Blueprint, redirect, render_template, request, url_for,abort
from flask_login import login_required
from marshmallow import Schema, fields
from app.service.projeto_service import fetch_projetos_ativos, add_projeto, fetch_projeto, edit_projeto as update_projeto, terminar_projeto, fetch_projetos_terminados
from app.service.tarefa_service import fetch_tarefas_projeto
from app.model.projeto import ProjetoModel
from app.model.tarefa import TarefaModel

projeto_bp = Blueprint('projeto', __name__)


@projeto_bp.route("/new", methods=['GET', 'POST'])
def create_projeto():
    if request.method == 'GET':
        return render_template("create_projeto.html")
    
    if request.method == 'POST':
        
        projeto = ProjetoModel(
            nome=request.form.get('nome'),
            descricao=request.form.get('descricao'),
            idGerente=request.form.get('idGerente'),
            idUsuarios=[]
        )
        try:
            add_projeto(projeto)
        except Exception as e:
            return render_template("create_projeto.html", error=str(e),projeto=projeto)
        return redirect(url_for('projeto.listar_projetos'))

#TODO Projetos ativos apenas do usuario logado

@projeto_bp.route("/list", methods=['GET'])
@login_required
def listar_projetos():
    projetos = fetch_projetos_ativos()
    return render_template("lista_projetos.html", projetos=projetos)

@projeto_bp.route("/details/<int:id>", methods=['GET'])
def projeto_detalhes(id):
    projeto = fetch_projeto(id)
    if projeto is None:
        return abort(404)
    tarefas = fetch_tarefas_projeto(id)
    return render_template('projeto_detalhes.html', projeto=projeto, tarefas=tarefas)

@projeto_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit_projeto_view(id):
    projeto = fetch_projeto(id)
    if projeto is None:
        return abort(404)
    
    if request.method == 'POST':
        
        try:
            projeto.nome = request.form.get('nome')
            projeto.descricao = request.form.get('descricao')
            projeto.data_inicio = request.form.get('data_inicio')
            projeto.idGerente = request.form.get('idGerente')
            update_projeto(projeto)
            return redirect(url_for('projeto.projeto_detalhes', id=projeto.idProjeto))
        except Exception as e:
            print("Erro:", e)
            return render_template("edit_projeto.html", projeto=projeto, error=str(e))
    
    return render_template("edit_projeto.html", projeto=projeto)

@projeto_bp.route("/terminate/<int:id>", methods=['GET'])
def terminar_projeto_view(id):
    terminar_projeto(id)
    return redirect(url_for('projeto.listar_projetos'))

@projeto_bp.route("/list/terminados", methods=['GET'])
def listar_projetos_terminados():
    projetos_terminados = fetch_projetos_terminados()
    return render_template("lista_projetos_terminados.html", projetos=projetos_terminados)