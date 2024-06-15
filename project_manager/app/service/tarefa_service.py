from app.db.tarefa import (
    get_all_tarefas,
    get_tarefa_by_id,
    create_tarefa,
    update_tarefa,
    delete_tarefa,
    get_usuario_tarefas,
    get_user_projeto_tarefas,
    get_projeto_tarefas,
)
from model.tarefa import TarefaModel
import datetime

def get_tarefas():
    return get_all_tarefas()

def get_tarefa(idTarefa):
    return get_tarefa_by_id(idTarefa)

def add_tarefa(tarefa: TarefaModel):
    tarefa.data_criacao = datetime.date.today()
    try:
        prazo_date = datetime.datetime.strptime(tarefa.prazo, "%Y-%m-%d").date()
        if prazo_date < tarefa.data_criacao:
            raise ValueError("Prazo cannot be earlier than the creation date")
    except ValueError:
        raise ValueError("Invalid prazo format. Please use YYYY-MM-DD")
    
    create_tarefa(tarefa.nome, tarefa.data_criacao, tarefa.descricao, tarefa.prazo, tarefa.status, tarefa.idProjeto, tarefa.idUsuarios)

def edit_tarefa(tarefa: TarefaModel):
    if tarefa.idTarefa is not None:
        update_tarefa(tarefa.idTarefa,
                       tarefa.nome,
                        tarefa.data_criacao,
                        tarefa.descricao,
                        tarefa.prazo,
                        tarefa.status,
                        tarefa.idProjeto,
                        tarefa.idUsuarios
                        )
    else:
        raise ValueError("<EditTarefa> Tarefa não encontrada")

def remove_tarefa(idTarefa):
    delete_tarefa(idTarefa)

def get_tarefas_usuario(idUsuario):
    return get_usuario_tarefas(idUsuario)

def get_tarefas_usuario_projeto(idUsuario, idProjeto):
    return get_user_projeto_tarefas(idUsuario, idProjeto)

def get_tarefas_projeto(idProjeto):
    return get_projeto_tarefas(idProjeto)