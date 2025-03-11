alunos =[
    {'nprocesso':123,'nome':'maria','email':'maria@gmail.com'},
    {'nprocesso':124,'nome':'joaquim','email':'joaquim@gmail.com'},
    {'nprocesso':125,'nome':'antónio','email':'antonio@gmail.com'}
]

notas = [
    {'nprocesso':alunos[0] ,'notas':[10,11,12,13]},
    {'nprocesso':alunos[1] ,'notas':[10,15,8,14]},
]

#mostrar o nome e as notas dos alunos
#os alunos sem notas não devem aparecer
for nota in notas:
    print(f"{nota['nprocesso']['nome']} - {nota['notas']}")

#apagar o primeiro aluno
del alunos[0]
print(alunos)

for nota in notas:
    print(f"{nota['nprocesso']['nome']} - {nota['notas']}")
