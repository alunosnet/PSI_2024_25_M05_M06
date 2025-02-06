#ler 10 frutas diferentes e as quantidades e guardar num dicionário
frutas={}

for i in range(3):
    fruta = input("Qual a fruta: ")
    quantidade = int(input("Qual a quantidade:"))
    frutas[fruta] = quantidade

print(frutas)

#ler a fruta a remover do dicionário
fruta_remover = input("Qual a fruta que não gostas? ")
if fruta_remover in frutas:
    del frutas[fruta_remover]
else:
    print("Essa fruta não existe no dicionário.")

#listar frutas do dicionário
for chave, valor in frutas.items():
    print(f"{chave} -> {valor}")

#mostrar o nome da fruta com a maior quantidade
maior = 0
maior_fruta=""
for chave, valor in frutas.items():
    if valor > maior:
        maior = valor
        maior_fruta = chave
print(f"A fruta com maior quantidade é {maior_fruta} com {maior}")