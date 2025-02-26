"""
Programa para gerir os livros de uma biblioteca e os seus empréstimos
"""
livros=["livro 1","livro 2","livro 3","livro 4"]
emprestimos=[]

def Listar(dados):
    for d in dados:
        print(d)
#o programa deve terminar quando é inserido um título em branco ou quando não há mais livros para emprestar
livro = input("Qual o livro a emprestar: ")
while livro != "":
    #avisar o utilizador quando o livro já está emprestado ou não existe
    if livro in livros:
        #remover da lista de livros para a lista de emprestimo
        livros.remove(livro)
        emprestimos.append(livro)
    elif livro in emprestimos:
        print("Livro está emprestado")
    else:
        print("Livro não existe")
    #mostrar os livros e os emprestimos
    Listar(livros)
    Listar(emprestimos)
    #verificar se ainda
    if len(livros)==0:
        print("Não tem mais livros para emprestar.")
        break 
    #ler o título do livro emprestar
    livro = input("Qual o livro a emprestar: ")

