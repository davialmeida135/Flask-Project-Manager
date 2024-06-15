class TarefaModel:
    def __init__(self, idTarefa=None, nome=None, data_criacao=None, descricao=None, prazo=None, status=None, idProjeto=None, idUsuarios=None,):
        self.idTarefa = idTarefa
        self.nome = nome
        self.data_criacao = data_criacao
        self.descricao = descricao
        self.prazo = prazo
        self.status = status
        self.idProjeto = idProjeto
        self.idUsuarios = idUsuarios

    def to_dict(self):
        return {
            'idTarefa': self.idTarefa,
            'nome': self.nome,
            'data_criacao': self.data_criacao,
            'descricao': self.descricao,
            'prazo': self.prazo,
            'status': self.status,
            'idProjeto': self.idProjeto,
            'idUsuarios': self.idUsuarios,
        }