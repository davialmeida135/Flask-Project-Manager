from app.db.tarefa import (
    create_tarefa,
    update_tarefa,
    delete_tarefa,
    get_all_tarefas,
    get_tarefa_by_id,
    get_usuario_tarefas,
    get_user_projeto_tarefas,
    get_projeto_tarefas,
    delete_tarefa_usuarios,
)
from app.model.tarefa import TarefaModel
import datetime

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
    delete_tarefa_usuarios(idTarefa)
    delete_tarefa(idTarefa)

def get_tarefas():
    return get_all_tarefas()

def get_tarefa(idTarefa):
    tarefa_data = get_tarefa_by_id(idTarefa)
    if tarefa_data:
        return TarefaModel(
            idTarefa=tarefa_data['idTarefa'],
            nome=tarefa_data['nome'],
            data_criacao=tarefa_data['data_criacao'],
            descricao=tarefa_data['descricao'],
            prazo=tarefa_data['prazo'],
            status=tarefa_data['status'],
            idProjeto=tarefa_data['idProjeto'],
            idUsuarios=tarefa_data.get('idUsuarios')
        )
    return None

def get_tarefas_usuario(idUsuario):
    return get_usuario_tarefas(idUsuario)

def get_tarefas_usuario_projeto(idUsuario, idProjeto):
    return get_user_projeto_tarefas(idUsuario, idProjeto)

def get_tarefas_projeto(idProjeto):
    return get_projeto_tarefas(idProjeto)