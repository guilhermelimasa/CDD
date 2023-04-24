alunos = int(input("digite o número de alunos da sala: "))
c = 1
soma = 0
while c <= alunos:
    nota = float(input("digite sua nota: "))
    c+=1
    soma = soma + nota
media = soma / alunos
print(media)