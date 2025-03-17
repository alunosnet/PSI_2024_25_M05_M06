"""
Trabalho Modelo - Módulo 6
--------------------------
Um programa para gerir livros e empréstimos de uma biblioteca
Requisitos funcionais:
    - Gestão livros (CRUD)
    - Gestão leitores (CRUD)
    - Empréstimos e devoluções
    - Estatísticas (empréstimos em atraso, top livros, top mês, top leitores, ...)
"""
import utils, livros, leitores

#Deve estar True quando em testes e False quando em produção
DEBUG =True

def MenuPrincipal():
    if DEBUG:
        livros.configurar()
        leitores.Configurar()
    op = 0
    while op!=5:
        op = utils.Menu(["Livros","Leitores","Empréstimos/devoluções","Estatísticas","Sair"],"Menu principal")
        if op == 5:
            break
        if op == 1:
            livros.MenuLivros()
        if op == 2:
            leitores.MenuLeitores()

if __name__=='__main__':
    MenuPrincipal()