from biblioteca import Biblioteca


def main():

    biblioteca = Biblioteca()

    op = 0
    while op != 6:
        print('\nSistema biblioteca')
        print('1 - Criar novo usuário: ')
        print('2 - Fazer empréstimo de livro')
        print('3 - Fazer devolução de livro')
        print('4 - Ver acervo da biblioteca')
        print('5 - Ver livros emprestados')
        print('6 - Sair do sistema')
        op = int(input('Digite a opção desejada: '))
        if op == 1:
            nome = input('Digite seu nome: ')
            email = input('Digite seu email: ')
            senha = input('Digite sua senha: ')
            biblioteca.adicionarUsuario(nome, email, senha)
        elif op == 2:
            email = input('Digite seu email: ')
            titulo = input('Digite o título do livro que deseja pegar emprestado: ')
            data_emp = input('Digite a data do empréstimo (dd//mm/aaaa): ')
            data_dev = input('Digite a data da devolução: (dd//mm/aaaa): ')
            biblioteca.fazerEmprestimo(email, titulo, data_emp, data_dev)
        elif op == 3:
            titulo = input('Digite o título do livro que deseja devolver: ')
            data_dev = input('Digite a data da devolução (dd/mm/aaaa): ')
            biblioteca.fazerDevolucao(titulo, data_dev)
        elif op == 4:
            biblioteca.verAcervo()
        elif op == 5:
            biblioteca.verLivrosEmprestados()
        elif op == 6:
            print('Obrigado por usar o sistema da biblioteca!')
            break
        else:
            print('Opção inválida! Tente novamente!')


main()
