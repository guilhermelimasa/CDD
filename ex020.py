lista = []
contador = 0
for c in range(10):
    lista.append(int(input("digite um número: ")))
x = int(input("digite um número para pesquisar: "))
for y in range(10):
    if lista[y] == x:
        contador += 1
print(f"o número apareceu {contador} vezes ")
