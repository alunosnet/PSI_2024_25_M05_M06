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
        if chave_pesquisar==chave[:len(chave_pesquisar)]:    #slicing para só comparar o inicio da chave
            print(f"{chave} -> {valor}")

def apagar(dicionario):
    #ler o termo a apagar
    chave_apagar = input("Introduza a palavra, ou parte da palavra, a apagar: ")
    #percorrer o dicionário
    for chave, valor in dicionario.items():
        #se o termo existir no inicio da chave mostrar o valor
        if chave_apagar==chave[:len(chave_apagar)]:    #slicing para só comparar o inicio da chave
            print(f"{chave} -> {valor}")
            op=input("Pretende remover esta palavra do dicionário? ")
            if op=='s':
                del dicionario[chave]
                return  #uma vez que o dicionário foi alterado não podemos continuar o ciclo

def configurar(dicionario):
    dicionario['pêra']='fruta'
    dicionario['pc']='computador pessoal'
    dicionario['bicicleta']='meio de transporte'
#se o programa está em desenvolvido deve ser True
#se está terminado (em produção) deve ser False
em_teste=True