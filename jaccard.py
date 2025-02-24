"""
Calcular o indice de Jaccard entre duas frase
https://en.wikipedia.org/wiki/Jaccard_index
"""
#ler as duas frases
frase1 = input("Introduza uma frase: ")
frase2 = input("Introduza uma frase: ")

#converter em conjuntos
frase1=frase1.lower().strip()
frase2=frase2.lower().strip()
conjuntoA = set(frase1.split(" "))
conjuntoB = set(frase2.split(" "))
#calcular a união
A_uniao_B = conjuntoA | conjuntoB
#calcular a interseção
A_inter_B = conjuntoA & conjuntoB

#dividir o nº de elementos da interseção pelo nº de elementos da união
indice=len(A_inter_B) / len(A_uniao_B)
print(indice)