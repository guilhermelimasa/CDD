num = int(input("digite um número: "))
contador = 1
cont = 0
zeca = 0
while contador < num:
    contador += 1
    if contador == 2:
        zeca += 1
        cont = 1
    elif contador % 2 == 0:
        continue
    elif contador % 3 == 0:
        continue
    elif contador % 5 == 0:
        continue
    elif contador % contador == 0:
        if cont == 1:
            cont = 0
            continue
        else:
            zeca += 1
            cont = 1

print(f"zeca tem {zeca} primos")


