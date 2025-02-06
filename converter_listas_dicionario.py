nomes = ["joaquim","maria","carlos"]
idades = [30,25,33]

#fazer um dicionário com os nomes como chave e as idades como valor
dicionario = dict(zip(nomes,idades))
print(dicionario)

for chave,valor in zip(nomes,idades):
    print(f"{chave} > {valor}")