cont = 0
somador = 0
while True:
    n = float(input("digite um número: "))
    cont += 1
    somador = somador+n
    if cont == 10:
        break
media = somador/10
print(media)
