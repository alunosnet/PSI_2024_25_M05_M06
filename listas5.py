#Conversão de listas em dicionários e o inverso
meu_dicionario={'nome':'joaquim','idade':15,'morada':'viseu'}

minha_lista = list(meu_dicionario.items())

print(minha_lista)

#converter duas listas num dicionário
chaves = ['nome','idade','morada']
valores = ['joaquim',16,'viseu']

dicionario = dict(zip(chaves,valores))
print(dicionario)