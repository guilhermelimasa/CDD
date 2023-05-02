x = int(input("digite um número: "))
if x % 2 == 0:
    if x > 0:
        print(f"{x} é um número par, e positivo.")
    else:
        print(f"{x} é um número par, e negativo.")
else:
    if x < 0:
        print(f"{x} é um número ímpar e negativo ")
    else:
        print(f"{x} é um número ímpar e positivo ")
