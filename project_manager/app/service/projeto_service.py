from app.db.projeto import (
    get_all_projetos,
    get_projeto_by_id,
    create_projeto,
    update_projeto,
    delete_projeto,
    get_projetos_usuario,
)
from model.projeto import ProjetoModel
import datetime

def get_projetos():
    return get_all_projetos()

def get_projeto(idProjeto):
    return get_projeto_by_id(idProjeto)

def add_projeto(projeto: ProjetoModel):
    projeto.data_criacao = datetime.date.today()
    create_projeto(projeto.idGerente,
                    projeto.data_inicio, 
                    projeto.nome,
                    projeto.descricao,
                    projeto.data_fim,
                    projeto.idUsuarios)

def edit_projeto(projeto: ProjetoModel):
    if projeto.idProjeto is not None:
        update_projeto(projeto.idGerente, 
                       projeto.data_inicio, 
                       projeto.nome,
                       projeto.descricao,
                       projeto.data_fim, 
                       projeto.idUsuarios
                       )
    else:
        raise ValueError("<EditProjeto> Projeto não encontrado")

def remove_projeto(idProjeto):
    delete_projeto(idProjeto)

def get_projetos_usuario(idUsuario):
    return get_projetos_usuario(idUsuario)