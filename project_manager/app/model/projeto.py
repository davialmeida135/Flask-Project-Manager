class ProjetoModel:
    def __init__(self, idProjeto=None, idGerente=None, data_inicio=None, nome=None, descricao=None, data_fim=None):
        self.idProjeto = idProjeto
        self.idGerente = idGerente
        self.data_inicio = data_inicio
        self.nome = nome
        self.descricao = descricao
        self.data_fim = data_fim

    def to_dict(self):
        return {
            'idProjeto': self.idProjeto,
            'idGerente': self.idGerente,
            'data_inicio': self.data_inicio,
            'nome': self.nome,
            'descricao': self.descricao,
            'data_fim': self.data_fim,
        }