#dicionário vazio
cidadao = {}

def LerDados(cidadao):
    #cria a chave e le o valor
    cidadao['nome'] = input("Introduza o nome:")
    cidadao['morada'] = input("Introduza a morada:")
    cidadao['cp'] = input("Introduza o código postal:")
    cidadao['idade'] = int(input("Introduza a idade:"))
    cidadao['pai'] = input("Nome do pai:")
    cidadao['mae'] = input("Nome da mãe:")
    op = input("Casado (s/n)")
    if op=='s':
        cidadao['casado']=True
    else:
        cidadao['casado']=False
    cidadao['nr_filhos'] = int(input("Nº de filhos:"))
    filhos = {}
    for filho in range(cidadao['nr_filhos']):
        chave = f"nome_{filho+1}"
        filhos[chave] = input(f"Introduza o nome do filho nº {filho+1}")
    print(filhos)
    cidadao["filhos"]=filhos

LerDados(cidadao)
print(cidadao)
#mostrar o nome do primeiro filho
print(cidadao["filhos"]["nome_1"])