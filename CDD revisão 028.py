vetor = []
somador = 0
contador = 0
for c in range(5):
    vetor.append(float(input("digite a nota: ")))
    somador = somador + vetor[c]
media = somador/5
for x in range(5):
    if vetor[x] >= media:
        contador += 1
print(f"a média da turma foi {media}, e {contador} notas ficaram acima da média.")