n = int(input("digite a quantidade de alunos na sala: "))
vetor = []
for c in range(n):
    vetor.append(str(input("digite o nome do aluno: ")))
for x in range(n):
    print(vetor[x])
    #print(vetor[x-1]) pra printar a lista de trás pra frente.
