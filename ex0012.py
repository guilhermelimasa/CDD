nalunos = int(input("digite o número de alunos: "))
lista_vazia = []
c = 0
for x in range(nalunos):
    c = c+1
    lista_vazia.append(input("digite o nome do aluno: "))
for y in range(lista_vazia):
    print(lista_vazia[y],y)


