from livro import Livro
from usuario import Usuario
from emprestimo import Emprestimo
import datetime


class Biblioteca:

    def __init__(self):
        self.acervo = []
        livro1 = Livro('DOM CASMURRO', 'MACHADO DE ASSIS', 'MODERNA')
        self.acervo.append(livro1)
        livro2 = Livro('O CORTIÇO', 'ALUISIO DE AZEVEDO', 'ATLAS')
        self.acervo.append(livro2)
        livro3 = Livro('O ALIENISTA', 'MACHADO DE ASSIS', 'MODERNA')
        self.acervo.append(livro3)

        self.usuarios = []

        self.emprestimos = []

    def adicionarUsuario(self, nome, email, senha):
        controle = True
        usuario_add = Usuario(nome, email, senha)
        for usuario in self.usuarios:
            if usuario_add.email == usuario.email:
                controle = False

        if controle:
            self.usuarios.append(usuario_add)
            print('Usuário cadastrado com sucesso!')
        else:
            print('Impossível adicionar! Usuário já cadastrado!')

    def verAcervo(self):
        print('\nA biblioteca possui os seguintes livros')
        for livro in self.acervo:
            print(livro)

    def verLivrosEmprestados(self):
        if len(self.emprestimos) == 0:
            print('\nNenhum livro da biblioteca está emprestado')
        else:
            print('\nA biblioteca possui os seguintes livros emprestados\n')
            for emprestimo in self.emprestimos:
                print(f'Livro: {emprestimo.livro} - Data devolução: {emprestimo.data_dev}')

    def fazerEmprestimo(self, email, titulo, data_emp, data_dev):
        controle_usuario = False
        controle_acervo = False
        controle_emp = True
        usuario_emp = Usuario('xxx', 'xxx', 'xxx')
        livro_emp = Livro('xxx', 'xxx', 'xxx')

        for usuario in self.usuarios:
            if email == usuario.email:
                controle_usuario = True
                usuario_emp = usuario

        for livro in self.acervo:
            if titulo.upper() == livro.titulo:
                controle_acervo = True
                livro_emp = livro

        for emprestimo in self.emprestimos:
            if titulo.upper() == emprestimo.livro.titulo:
                controle_emp = False

        if (controle_usuario and controle_acervo) and controle_emp:
            self.emprestimos.append(Emprestimo(usuario_emp, livro_emp, data_emp, data_dev))
            print('Emprestimo efetuado com sucesso!')
        elif not controle_usuario:
            print('Erro ao efetuar empréstimo! Usuário não cadastrado!')
        elif not controle_acervo:
            print('Erro ao efetuar empréstimo! Livro não consta no acervo da biblioteca!')
        elif not controle_emp:
            print('Erro ao efetuar empréstimo! Livro já emprestado! Aguarde Devolução!')

    def fazerDevolucao(self, titulo, data_dev):

        controle_emp = False

        for emprestimo in self.emprestimos:
            if titulo.upper() == emprestimo.livro.titulo:
                controle_emp = True
                self.emprestimos.remove(emprestimo)

        if controle_emp:
            print(f'Livro devolvido com sucesso em {data_dev}')
        else:
            print('Erro na devolução! O livro não está emprestado ou não existe no acervo da biblioteca!')
            print('Tente novamente!')
