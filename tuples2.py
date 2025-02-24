vencimentos = (1000,5000,2500,1350,4750,850)
nomes       = ("A","B","C","D","E","F")

#utilizando uma função
"""calcular e devolver a soma de todos os vencimentos,o maior e o menor
"""
def SomarMaiorMenor(vencimentos):
    soma = sum(vencimentos)
    maior = max(vencimentos)
    menor = min(vencimentos)
    return (soma, maior, menor) #devolve um tuple
#desempacotamento do tuple
soma, maior, menor = SomarMaiorMenor(vencimentos)
print(f"A soma total dos vencimentos é {soma}, o maior vencimento é {maior} e o menor é {menor}")
#calcular e mostrar a média dos vencimentos
media = soma / len(vencimentos)
print(f"A média dos vencimentos é de {media}")
#mostrar o nome de quem tem o maior vencimento
posicao = vencimentos.index(maior)
print(f"{nomes[posicao]} é o que tem o maior vencimento!")