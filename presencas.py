"""
Um programa que calcula:
- os alunos que estiveram presentes todos os dias
- os alunos que faltaram pelo menos um dia
- os alunos que só estiveram presentes na segunda e na sexta, mas não estiveram na terça, quarta ou quinta
"""
#conjuntos com os alunos presentes em cada dia da semana
segunda = {"Ana", "Carlos", "Pedro", "Maria"}
terca = {"Ana", "João", "Clara"}
quarta = {"Maria", "Ana", "Paulo"}
quinta = {"João", "Clara", "Paulo", "Ana"}
sexta = {"Ana", "Maria", "Carlos", "Paulo"}

#os alunos que estiveram presentes todos os dias
todos_dias = segunda.intersection(terca,quarta,quinta,sexta)
print(f"Alunos presentes em todos os dias {todos_dias}")
#os alunos que faltaram pelo menos um dia
todos_alunos = segunda.union(terca,quarta,quinta,sexta)
alunos_faltaram = todos_alunos.difference(todos_dias)
print(f"Alunos que faltaram pelo menos um dia {alunos_faltaram}")
#os alunos que só estiveram presentes na segunda e na sexta, mas não estiveram na terça, quarta ou quinta
segunda_sexta = segunda & sexta #& interseção
t_q_q = terca | quarta | quinta #| união
presentes_s_s = segunda_sexta - t_q_q   #- diferença
print(presentes_s_s)