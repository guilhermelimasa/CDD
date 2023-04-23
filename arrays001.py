alunos = int(input("digite o número de alunos na sala: "))
lista = []
contador = 0
for x in range(alunos):
    lista.append(input("digite o nome do aluno: "))
    contador = +1
for y in range(alunos):
    print(lista[y],y)
