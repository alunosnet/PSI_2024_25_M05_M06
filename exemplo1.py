#definir um dicionário utilizamos { chave: valor }

dicionario = {'nome' : 'Joaquim'}

print(dicionario['nome'])
#alterar o valor de uma chave
dicionario['nome'] = input("Introduza um nome:")
print(dicionario['nome'])

#adicionar novas chaves:valores
dicionario['idade'] = 10
#chaves e valores podem ser string ou números
dicionario[10] ='blabla'
print(dicionario)

#fazer um ciclo para percorrer os pares chaves:valores
chaves = dicionario.keys()      #devolve uma lista com as chaves
valores = dicionario.values()   #devolve uma lista com os valores
elementos = dicionario.items()    #devolve uma lista com os pares chaves:Valores
print(chaves,elementos)
for chave in dicionario.keys():
    print(dicionario[chave])
#ciclo percorre os items do dicionario (chave:valor)
for pares in dicionario.items():
    print(f"{pares[0]} : {pares[1]}")

#remover chaves:valores do dicionário
valor = dicionario.pop("idade",None)
print(f"Idade (removida): {valor}") #primeira vez deve devolver 10
print(dicionario)
valor = dicionario.pop("idade",None)
print(f"Idade (removida): {valor}") #segunda vez devolve None porque a chave já não existe
#remove a chave indicada entre []
del dicionario['nome']
print(dicionario)
