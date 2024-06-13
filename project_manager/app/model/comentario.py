class ComentarioModel:
    def __init__(self, idComentario=None, mensagem=None, idUsuario=None, idTarefa=None, idDestinatario=None):
        self.idComentario = idComentario
        self.mensagem = mensagem
        self.idUsuario = idUsuario
        self.idTarefa = idTarefa
        self.idDestinatario = idDestinatario

    def to_dict(self):
        return {
            'idComentario': self.idComentario,
            'mensagem': self.mensagem,
            'idUsuario': self.idUsuario,
            'idTarefa': self.idTarefa,
            'idDestinatario': self.idDestinatario,
        }