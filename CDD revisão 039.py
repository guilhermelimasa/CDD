a = []
for x in range(10):
    a.append(int(input(f'Digite um número: ')))
for impares in range(10):
    if a[impares] % 2 != 0:
        print(a[impares], end=' ')
print()
for pares in range(10):
    if a[pares] % 2 == 0 and a[pares] != 0:
        print(a[pares], end=' ')
print()
for positivo in range(10):
    if a[positivo] > 0:
        print(a[positivo], end=' ')
print()
for negativo in range(10):
    if a[negativo] < 0:
        print(a[negativo], end=' ')
print()
for zeros in range(10):
    if a[zeros] == 0:
        print(a[zeros], end=' ')
print()
