n = int(input("digite a quantidade de alunos na sala: "))
vetor = []
contador = 0
for c in range(n):
    vetor.append(str(input("digite o nome do aluno: ")))
aluno = input("qual o nome do aluno que vc quer procurar?")
for x in range(n):
    contador += 1
    if aluno in vetor[x]:
        print(f"{vetor[x]}-{contador}")
