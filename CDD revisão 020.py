n = int(input("digite a quantidade de alunos da sala: "))
cont = 0
somador = 0
while True:
    nota = int(input("digite a nota: "))
    cont +=1
    somador = somador + nota
    if cont == n:
        break
media = somador / n
print(f"a média da turma é {media}")


