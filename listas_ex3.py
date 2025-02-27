"""
Programa para gerir o stock de produtos. De cada vez que um produto é vendido o stock deve baixar e de cada vez que um produto é comprado o stock aumenta.
Exemplo:
    vender 10 batatas   - reduz o stock das batatas em 10
    comprar 50 bananas  - aumenta o stock das bananas em 50
    consultar batatas   - deve mostrar o stock disponível de batatas 
    terminar            - termina o programa
Se for inserido um comando não conhecido deve ser apresentada uma mensagem de erro
De cada vez que é realizada uma operação deve ser indicado o stock remanescente incluindo a unidade de medida (de acordo com o Afonso & Afonso)
Não deve possível vender stock que não existe e não deve ser possível comprar valores negativos de stock
hacker:
- adicionar uma lista com preços unitários e mostrar em cada operação o valor total a receber/pagar (sugestão do Gabriel)
- adicionar a possibilidade de comprar produtos novos
"""
produtos = ["batatas","bananas","arroz"     ,"bacalhau","maçãs"]
stock    = [10       , 50      , 10         , 5        , 5]
unidades = ["kg"     , "kg"    , "embalagem", "unidade", "kg" ]

def Existe(produto):
    """Mostra erro e devolve false se não existir"""
    if produto not in produtos:
        print("Produto não existe.")
        return False
    return True

def Vender(produto,quantidade):
    """Recebe o produto e a quantidade a vender, atualiza e mostra o stock"""
    if Existe(produto) == False:
        return
    quantidade = int(quantidade)
    posicao = produtos.index(produto)
    quantidade_stock = stock[posicao]
    if quantidade_stock < quantidade:
        print("Não existe quantidade suficiente disponível.")
        return
    stock[posicao] -= quantidade
    print(f"Venda registada com sucesso. Ficou com {stock[posicao]}{unidades[posicao]} de {produto}.")

def Comprar(produto,quantidade):
    """Recebe o produto e a quantidade comprar, atualiza o stock e mostra o stock atualizado"""
    if Existe(produto) == False:
        op = input("Pretende adicionar este produto?")
        if op in "sS":
            produtos.append(produto)
            stock.append(int(quantidade))
            unidades.append(input("Qual a unidade de medida?"))
        return
    quantidade = int(quantidade)
    posicao = produtos.index(produto)
    stock[posicao] += quantidade
    print(f"Compra registada com sucesso. Ficou com {stock[posicao]}{unidades[posicao]} de {produto}")

def Consultar(produto):
    """Recebe o produto e mostra a quantidade em stock"""
    if Existe(produto) == False:
        return
    posicao = produtos.index(produto)
    print(f"Tem {stock[posicao]}{unidades[posicao]} de {produtos[posicao]} em stock")

def Comando(texto):
    """Recebe o texto inserido e devolve um tuple com o comando a quantidade e o produto
        Devolve False quando o comando é terminar
    """
    texto = texto.strip().lower()
    if len(texto)==0:
        return True
    if texto=='terminar':
        return False
    partes = texto.split(" ")
    if len(partes)<2 or len(partes)>3:
        print("Comando não é válido")
        return True
    if partes[0] not in ("vender","comprar","consultar"):
        print("Comando não é válido")
        return True
    if partes[0]=="consultar":
        Consultar(partes[1])
    if partes[0]=="vender":
        #comando necessita de 3 partes e a segunda tem de ser um nº
        if (len(partes)!=3 or partes[1].isdigit()==False):
            print("Comando não é válido")
            return True
        Vender(partes[2],partes[1])
    if partes[0]=="comprar":
        #comando necessita de 3 partes e a segunda tem de ser um nº
        if (len(partes)!=3 or partes[1].isdigit()==False):
            print("Comando não é válido")
            return True
        Comprar(partes[2],partes[1])

def main():
    """Ciclo que lê os comandos"""
    linha = input("Introduza um comando:")
    while Comando(linha)!=False:
        linha = input("Introduza um comando:")   

if __name__ == '__main__':
    main()