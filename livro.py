class Livro:

    def __init__(self, titulo, autor, editora):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora

    def __str__(self):
        return f'Titulo: {self.titulo} - Autor: {self.autor} - Editora: {self.editora}'
