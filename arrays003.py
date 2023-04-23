lista = []
somador = 0
contador = 0
for c in range(5):
    lista.append(int(input("digite sua nota: ")))
    somador = somador + lista[c]
    if lista[c] >= 7:
        contador += 1
media = somador / 5
print(f"a média da sala foi {media} e {contador} alunos ficaram acima da média.")