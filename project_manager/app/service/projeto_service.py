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

def get_projetos():
    return get_all_projetos()

def get_projeto(idProjeto):
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

def get_projetos_usuario(idUsuario):
    return get_projetos_usuario(idUsuario)