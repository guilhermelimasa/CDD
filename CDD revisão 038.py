a = []
contador = 0
somador = 0
while contador < 10:
    somador += 1
    if somador % 2 != 0:
        a.append(somador)
        contador += 1
print(a)
