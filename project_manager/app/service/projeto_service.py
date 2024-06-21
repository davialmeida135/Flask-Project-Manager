from app.db.projeto import (
    get_all_projetos,
    get_projeto_by_id,
    create_projeto,
    update_projeto as update_db_projeto,
    delete_projeto,
    get_projetos_usuario as fetch_projetos_usuario,
    adicionar_usuario_projeto,
    remover_usuario_projeto
)
from app.service.usuario_service import get_usuario_by_id
from app.model.projeto import ProjetoModel
import datetime

def fetch_projetos():
    projetos_data = get_all_projetos()
    projetos = [ProjetoModel(
        idProjeto=projeto['idProjeto'],
        idGerente=projeto['idGerente'],
        data_inicio=projeto['data_inicio'],
        nome=projeto['nome'],
        descricao=projeto['descricao'],
        data_fim=projeto['data_fim'],
        idUsuarios=projeto.get('idUsuarios', [])
    ) for projeto in projetos_data]
    return projetos

def fetch_projeto(idProjeto):
    projeto_data = get_projeto_by_id(idProjeto)
    if projeto_data:
        return ProjetoModel(
            idProjeto=projeto_data['idProjeto'],
            idGerente=projeto_data['idGerente'],
            data_inicio=projeto_data['data_inicio'],
            nome=projeto_data['nome'],
            descricao=projeto_data['descricao'],
            data_fim=projeto_data['data_fim'],
            idUsuarios=projeto_data.get('idUsuarios', [])
        )
    return None

def add_projeto(projeto: ProjetoModel):
    print(f"Adicionando projeto: {projeto.to_dict()}")  # Mensagem de depuração
    projeto.data_inicio = datetime.date.today()
    create_projeto(projeto.idGerente,
                   projeto.data_inicio,
                   projeto.nome,
                   projeto.descricao,
                   projeto.data_fim,
                   projeto.idUsuarios)

def edit_projeto(projeto: ProjetoModel):
    if projeto.idProjeto is not None:
        update_db_projeto(projeto.idProjeto,
                          projeto.idGerente,
                          projeto.data_inicio,
                          projeto.nome,
                          projeto.descricao,
                          projeto.data_fim)
    else:
        raise ValueError("<EditProjeto> Projeto não encontrado")

def remove_projeto(idProjeto):
    delete_projeto(idProjeto)

def terminar_projeto(idProjeto):
    projeto = fetch_projeto(idProjeto)
    if projeto:
        projeto.data_fim = datetime.date.today()
        edit_projeto(projeto)
    else:
        print(f"Projeto com id {idProjeto} não encontrado")

def get_projetos_ativos(idUsuario):
    projetos_data = fetch_projetos_usuario(idUsuario)
    projetos = [ProjetoModel(**projeto) for projeto in projetos_data]
    projetos_ativos = [projeto for projeto in projetos if projeto.data_fim is None]
    return projetos_ativos

def get_projetos_terminados(idUsuario):
    projetos_data = fetch_projetos_usuario(idUsuario)
    projetos = [ProjetoModel(**projeto) for projeto in projetos_data]
    projetos_terminados = [projeto for projeto in projetos if projeto.data_fim is not None]
    return projetos_terminados

def adicionar_usuario(usuario_id, projeto_id):    
    adicionar_usuario_projeto(usuario_id, projeto_id)

def remover_usuario(idUsuario, idProjeto):
    remover_usuario_projeto(idUsuario, idProjeto)
