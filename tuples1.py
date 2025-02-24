"""
Crie um tuple com os nomes dos meses do ano.
Mostrar o terceiro mês do ano.
Obtenha o tuple dos meses de verão (junho, julho, agosto, setembro).
Verifique se "Junho" está presente no tuplo de meses de verão.
Extra:
listar os meses por ordem alfabética
Mostrar os meses cujo nome começa por j
Mostrar o mes(es) com o maior nome
"""
meses = ("janeiro","fevereiro","março","abril","maio","junho", 
         "julho","agosto","setembro","outubro","novembro","dezembro")
#terceiro mês
print(meses[2])
#meses do verão
verao = meses[5:9]
print(verao)
#junho faz parte do verão?
if "junho" in verao:
    print("junho faz parte do verão")
else:
    print("junho não faz parte do verão")

#listar os meses por ordem alfabética
meses_sort = sorted(meses)
print(meses_sort)

#listar os meses que começam por j
for mes in meses:
    if mes[0]=="j":
        print(mes)

#Mostar o mes(es) com o maior nome
maior=meses[0]
for mes in meses:
    if len(maior) < len(mes):
        maior = mes
print(maior)