a = []
contador = 0
somador = 0
while contador <= 20:
    somador -= 1
    if somador <= 0:
        a.append(somador)
        contador += 1
for x in range(20):
    print(a[x])
