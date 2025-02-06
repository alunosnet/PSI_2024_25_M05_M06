"""
Programa que implementa as funcionalidades de um dicionário de termos técnicos (termo e definição)
Menu de opções (1. Adicionar termo;2. Listar todos os termos;3. Pesquisar um termo;4. Apagar um termo;5. Sair)
Opcional: Listar todos os termos ordenados alfabeticamente
No futuro: Guardar os dados num ficheiro (M07)
"""
def adicionar(dicionario):
    #ler o termo
    termo = input("Qual a palavra a adicionar ao dicionário? ")
    #verificar se já existe
    if termo in dicionario:
        #se existir perguntar se pretende atualizar
        op = input("Esse termo já existe no dicionário. Pretende alterar? ")
        if op=='n':
            return
    #ler a definição
    definicao = input("Qual a definição da palavra indicada? ")
    #adicionar ou atualizar o dicionário
    dicionario[termo]=definicao
    print("Termo adicionado/atualizado com sucesso")

def listar(dicionario):
    #for chave in dicionario.keys():
    #    print(f"{chave} -> {dicionario[chave]}")
    op = input("Pretende visualizar por ordem alfabética? ")
    if op!='s':
        for chave, valor in dicionario.items():
            print(f"{chave} -> {valor}")
    else:
        #ordenar as chaves
        chaves = dicionario.keys()
        chaves = sorted(chaves)
        #percorrer as chaves ordenadas e mostrar o valor correspondente
        for chave in chaves:
            print(f"{chave} -> {dicionario[chave]}")

def pesquisar(dicionario):
    #ler o termo a pesquisar
    chave_pesquisar = input("Introduza a palavra, ou parte da palavra, a pesquisar: ")
    #percorrer o dicionário
    for chave, valor in dicionario.items():
        #se o termo existir no inicio da chave mostrar o valor
        if chave_pesquisar==chave[len(chave_pesquisar)]:    #slicing para só comparar o inicio da chave
            print(f"{chave} -> {valor}")

def apagar(dicionario):
    pass

def configurar(dicionario):
    dicionario['pêra']='fruta'
    dicionario['pc']='computador pessoal'
    dicionario['bicicleta']='meio de transporte'
#se o programa está em desenvolvido deve ser True
#se está terminado (em produção) deve ser False
em_teste=True

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