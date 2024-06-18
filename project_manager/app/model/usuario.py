from flask_login import UserMixin


class UsuarioModel(UserMixin):
    def __init__(self, id=None, nome= None, username = None, password = None):
        self.id = id
        self.nome = nome
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            'idUsuario': self.idUsuario,
            'nome': self.nome,
            'username': self.username,
            #'password': self.password
        }