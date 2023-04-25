lista = []
for c in range(5):
    lista.append(float(input("digite um número: ")))
x = float(input("digite um número: "))
contador = 0
for y in range(5):
    if lista[y] == x:
       contador+=1
print(f"o número {x} aparece {contador} vezes")