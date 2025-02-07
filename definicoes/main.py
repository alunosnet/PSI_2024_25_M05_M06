"""
Programa que implementa as funcionalidades de um dicionário de termos técnicos (termo e definição)
Menu de opções (1. Adicionar termo;2. Listar todos os termos;3. Pesquisar um termo;4. Apagar um termo;5. Sair)
Opcional: Listar todos os termos ordenados alfabeticamente
No futuro: Guardar os dados num ficheiro (M07)
"""
from dicionario import configurar,adicionar,listar,pesquisar,apagar,em_teste

def menu():
    dicionario = {}
    if em_teste:
        configurar(dicionario)
    op = 0
    while op!=5:
        print("1.Adicionar\n2.Listar\n3.Pesquisar\n4.Apagar\n5.Sair")
        op = int(input("Opção:"))
        if op == 1:
            adicionar(dicionario)
        elif op==2:
            listar(dicionario)
        elif op==3:
            pesquisar(dicionario)
        elif op==4:
            apagar(dicionario)
        elif op==5:
            print("Obrigado por utilizar o nosso programa.")
        else:
            print("Opção inválida")

if __name__=='__main__':
    menu()