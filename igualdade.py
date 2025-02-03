carro1 = {'marca':'ford','cor':'azul','lugares':5}
carro2 = {'cor':'azul', 'marca':'ford','lugares':4}
carro2 = {'cor':'azul', 'marca':'ford'}

#dois dicionários são iguais quando têm as mesmas chaves e valores
#a ordem destes não interessa
if carro1 == carro2:
    print("Carros iguais")
else:
    print("Carros diferentes")