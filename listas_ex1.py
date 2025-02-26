"""
Programa para ler as marcas de carros de um stand. O programa deve mostrar qual a marca com mais veículos.
- Ler do utilizador as marcas e guardar numa lista
- Parar de ler quando o utilizador inserir uma marca vazia
- Calcular para cada marca quantos carros existem
- Mostrar a marca com mais carros
(utilizar listas para guardar as marcas)
"""
carros = [] #lista para guardar a marca dos carros

#fazer um ciclo para ler a marca e adicionar à lista
#o ciclo termina quando a marca == ""
marca=" "
while marca!="":
    marca = input("Introduza uma marca: ")
    if marca!="":
        carros.append(marca)

#contar quantos carros existem de cada marca
marcas = set(carros)    #cria um set com as marcas (sem repetições)
maior = 0
mmaior = ""
for marca in marcas:
    contar = carros.count(marca)
    print(f"Da marca {marca} tem {contar} carros")
    if contar > maior:
        mmaior = marca
        maior = contar
print(f"A marca {mmaior} é a que tem mais veículos com {maior} carros")

#remover todos os veículos da marca indicada pelo utilizador
marca_remover=input("Qual a marca que deseja remover? ")
while marca_remover in carros:
    carros.remove(marca_remover)

print(carros)
