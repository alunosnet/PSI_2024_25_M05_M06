"""
Módulo de gestão dos livros
"""
import utils, app

#lista dos livros
livros = []

#Menu Livros
def MenuLivros():
    """Submenu para gerir os livros"""
    op = 0
    while op!=6:
        op = utils.Menu(["Adicionar","Listar","Editar","Apagar","Pesquisar","Voltar"],"Menu de livros")
        if op == 6:
            break

#Adicionar Livro
def Adicionar():
    pass #TODO: continuar AQUI!
#Editar Livro

#Apagar Livro

#Listar Livros

#Pesquisar Livros