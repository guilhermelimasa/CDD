n = int(input("digite a quantidade de alunos na sala: "))
vetor = []
contador = 0
for c in range(n):
    vetor.append(str(input("digite o nome do aluno: ")))
for x in range(n):
    contador +=1
    print(f"{vetor[x]}-{contador}")