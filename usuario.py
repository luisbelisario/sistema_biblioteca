class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


    def __str__(self):
        return f'Nome: {self.nome} - Email: {self.email}'
