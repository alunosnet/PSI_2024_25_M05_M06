"""
Módulo Empréstimos e devolucoes
"""
import utils, livros, leitores
from datetime import datetime, timedelta

# livro ({}), leitor ({}), data_emprestimo, data_devolucao, estado
emprestimos=[]

def MenuEmprestimos():
    op = 0
    while op != 3:
        op = utils.Menu(["Empréstimos","Devolução","Voltar"],"Menu de empréstimos/devolucoes")
        if op == 3:
            break
        if op == 1:
            Emprestimo()
        if op == 2:
            Devolucao()

def Emprestimo():
    #dados no empréstimo a adicionar à lista
    novo = {}
    # ler qual o livro a emprestar
    print("Indique o livro a emprestar: ")
    livro_emprestar = livros.pesquisar()
    if len(livro_emprestar)==0:
        print("Nenhum livro encontrado.Tente novamente.")
        return
    elif len(livro_emprestar)>1:
        #mostrar os livros encontrados
        livros.Listar(livro_emprestar)
        #pedir o id do livro a emprestar
        id = utils.ler_numero_inteiro("Introduza o id do livro a emprestar: ")
        for livro in livro_emprestar:
            if livro['id'] == id:
                if livro['estado'] != 'disponível':
                    print("Esse livro está emprestado.")
                    return
                novo['livro'] = livro
                break
        if 'livro' not in novo:
            print("O id indicado não existe")
            return
    else:
        #só encontrou um livro
        if livro_emprestar[0]['estado'] != 'disponível':
            print("Esse livro está emprestado.")
            return
        novo['livro'] = livro_emprestar[0]
    
    # ler qual o leitor que leva o livro
    print("Indique o leitor:")
    leitor_emprestimo = leitores.Pesquisar()
    if len(leitor_emprestimo)==0:
        print("Leitor não encontrado")
        return
    elif len(leitor_emprestimo)>1:
        print("Leitores encontrados:")
        leitores.Listar(leitor_emprestimo)
        id = utils.ler_numero_inteiro("Indique o id do leitor: ")
        for leitor in leitor_emprestimo:
            if leitor['id'] == id:
                novo['leitor'] = leitor
                break
        if 'leitor' not in novo:
            print("O id indicado não existe.")
    else:
        novo['leitor'] = leitor_emprestimo[0]
    #TODO: verificar se o leitor pode levar o livro
    # registar o empréstimo com data de devolução
    data_atual      = datetime.now()
    data_entrega    = data_atual + timedelta(days=30)
    str_data_atual  = data_atual.strftime("%Y-%m-%d")
    str_dta_entrega = data_entrega.strftime("%Y-%m-%d")
    novo['data_emprestimo'] = str_data_atual
    novo['data_devolucao'] = str_dta_entrega
    emprestimos.append(novo)
    # atualizar o estado do livro
    novo['livro']['estado'] = 'emprestado'
    novo['livro']['leitor'] = novo['leitor']
    print("Empréstimo registado com sucesso.")

def Devolucao():
    # ler o id do livro a devolver
    id_livro = utils.ler_numero_inteiro("Indique o id do livro a devolver:")
    # verificar se o livro está emprestado
    livro = livros.GetLivro(id_livro)
    if livro == None:
        print("Não existe nenhum livro com o id indicado")
    if livro['estado'] != 'emprestado':
        print("Esse livro não está emprestado")
    # verificar se a devolução está dentro prazo
    # registas se houve infração do leitor
    # atualizar o nr de empréstimo do livro
    livro['nr_emprestimos'] += 1
    # mudar o estado do livro
    livro['estado'] = 'disponível'
    livro['leitor'] = None
    # mudar o estado do empréstimo