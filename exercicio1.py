"""
Um programa para mostrar a capital de um país introduzido pelo utilizador
"""
capitais = { 'Portugal' : 'Lisboa',
             'Espanha' : 'Madrid',
            'França': 'Paris',
            'Brasil' : 'Brasilia',
            'Inglaterra' :'Londres',
             'Itália' : 'Roma' }

#perguntar ao utilizador o país
pais = input("Indique o país:")
# if pais not in capitais:
#     print("Não tenho informações sobre esse país")
# else:
#     #mostrar a capital correspondente
#     print(capitais[pais])

#utilizar a função get - devolve o valor da chave ou um valor por omissão no caso da chave não existir
print(capitais.get(pais,"Não tenho informações sobre esse país"))
