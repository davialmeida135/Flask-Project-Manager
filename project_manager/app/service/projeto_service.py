from app.db.projeto import (
    get_all_projetos,
    get_projeto_by_id,
    create_projeto,
    update_projeto,
    delete_projeto,
    get_projetos_usuario,
)
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
    print(f"Adicionando projeto: {projeto.to_dict()}")
    projeto.data_inicio = datetime.date.today()
    create_projeto(projeto.idGerente,
                   projeto.data_inicio,
                   projeto.nome,
                   projeto.descricao,
                   projeto.data_fim,
                   projeto.idUsuarios)

def edit_projeto(projeto: ProjetoModel):
    if projeto.idProjeto is not None:
        update_projeto(projeto.idProjeto,
                       projeto.idGerente,
                       projeto.data_inicio,
                       projeto.nome,
                       projeto.descricao,
                       projeto.data_fim,
                       projeto.idUsuarios)
    else:
        raise ValueError("<EditProjeto> Projeto não encontrado")

def remove_projeto(idProjeto):
    delete_projeto(idProjeto)

def fetch_projetos_usuario(idUsuario):
    return get_projetos_usuario(idUsuario)

def terminar_projeto(idProjeto):
    projeto = fetch_projeto(idProjeto)
    projeto.data_fim = datetime.date.today()
    edit_projeto(projeto)

def fetch_projetos_ativos():
    projetos = fetch_projetos()
    projetos = [projeto for projeto in projetos if projeto.data_fim is None]
    return projetos

def fetch_projetos_terminados():
    projetos = fetch_projetos()
    projetos_terminados = [projeto for projeto in projetos if projeto.data_fim is not None]
    return projetos_terminados