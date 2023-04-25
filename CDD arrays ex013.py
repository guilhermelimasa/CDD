lista = []
numero = 0
maior = 0
menor = 0
somador = 0
contador = 0
for c in range(5):
    lista.append(int(input("digite um número: ")))
for x in range(5):
    if lista[x] % 2 == 0:
        print(lista[x]," é um número par.")
for z in range(5):
    if numero == 0:
     maior = lista[z]
     menor = lista[z]
    numero = 1
    if lista[z] > maior:
        maior = lista[z]
    if lista[z] < menor:
        menor = lista[z]
print(f"o maior número é {maior} e o menor é {menor}.")
for v in range(5):
    somador = somador + lista[v]
    media = somador / 5
    if lista[v] >= media:
        contador +=1
print(f"a média das notas é {media} e {contador} notas estão acima da média.")


