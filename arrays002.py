alunos = int(input("digite o número de alunos na sala: "))
lista = []
contador = 0
for x in range(alunos):
    lista.append(input(f"digite o nome do {x+1} aluno: "))
    contador = +1
nome = input("qual aluno vc deseja saber a posição: ")

for y in range(alunos):
    if lista[y] == nome:
        print(f"{lista[y]} está na posição {y}")
