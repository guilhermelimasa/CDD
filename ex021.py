lista = []
maior = 0
menor = 0
somador = 0
contador = 0
for c in range(10):
    lista.append(int(input("digite um número: ")))
print(20*"-")
for x in range(10):
    if lista[x] % 2==0:
        print(f"os números pares são: {lista[x]}")
print(20*"-")
maior = lista[0]
menor = lista[0]
for v in range(10):
     if lista[v]>maior:
        maior = lista[v]
     if lista[v]<menor:
        menor = lista[v]
print(f"os maior número é {maior} e o menor é {menor} ")
print(20*"-")
for z in range(10):
    somador = somador + lista[z]
media = somador / 10
for h in range(10):
    if lista[h] > media:
        contador+=1
print(f"a média é {media} e {contador} estão acima da média.")

