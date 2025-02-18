"""
Sets (conjuntos)
Únicos (os elementos repetidos são descartados), não ordenados (não têm uma ordem fixa), mútaveis (adicionar, remover), elementos imutáveis (bool, int, float, string)
"""
#Definir
nomes_1 = {'maria','joão'}
nomes_2 = {'joão','joaquim','carlos'}
nomes_3 = {'joão','maria'}

#igualdade
if nomes_1 == nomes_3: #iguais porque a ordem dos eleemntos não conta
    print("São iguais")
else:
    print("São diferentes")

#União
nomes = nomes_1.union(nomes_2) #faz a união e devolve sem alterar
print("União: ",nomes)
nomes_v2 = nomes_1 | nomes_2 #faz a união e devolve sem alterar
print("União: ",nomes_v2)
nomes_1.update(nomes_2) #faz a união e altera
print("União: ",nomes_1)

#Interseção
nomes_iguais = nomes_3.intersection(nomes_2) #devolve a interseção sem alterar
print("Interseção: ",nomes_iguais)
nomes_iguais_v2 = nomes_3 & nomes_2 #devolve a interseção sem alterar
print("Interseção: ",nomes_iguais_v2)
nomes_1.intersection_update(nomes_3) #faz a interseção alterando
print("Interseção: ",nomes_1)

#Diferença
diferenca = nomes_3.difference(nomes_2)
print(f"{nomes_3} - {nomes_2} => Diferença: ",diferenca)
diferenca = nomes_2.difference(nomes_3)
print(f"{nomes_2} - {nomes_3} => Diferença: ",diferenca)
diferenca = nomes_2 - nomes_3
print(f"{nomes_2} - {nomes_3} => Diferença: ",diferenca)

#diferença simétrica
diferenca_simetrica = nomes_3.symmetric_difference(nomes_2)
print(f"{nomes_2} - {nomes_3} => Diferença simétrica: ",diferenca_simetrica)
diferenca_simetrica = nomes_2.symmetric_difference(nomes_3)
print(f"{nomes_3} - {nomes_2} => Diferença simétrica: ",diferenca_simetrica)
diferenca_simetrica = nomes_2 ^ nomes_3
print(f"{nomes_3} - {nomes_2} => Diferença simétrica: ",diferenca_simetrica)

#converter
valores = set([1,2,3,4,4,5,6,7,7,8])
print(valores)

#listar os valores
for x in valores:
    print(x)

#print(valores[1]) #não funciona
for p, valor in enumerate(valores,start=1):
    print(f"Elemento da posição {p}: {valor}")

#testar se existe
if 2 in valores:
    print("Existe o valor 2")
else:
    print("Não existe o valor 2")

#nº de elementos
print(len(nomes_3))