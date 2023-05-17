#if (n / 1) % 2 == 0:
#     if (n/2) % 2 == 0:
      #else:
      #print(f"{n} é um número primo")
def kdena(numero):
    while True:
        n = int(input("digite um número: "))
        if n % 2 == 0:
            if n == 2:
                print("este número é primo")
            else:
                print(f"este número n é primo.")
        elif n % 3 == 0:
            if n == 3:
                print("este número é primo.")
            else:
                print(f"este número n é primo.")
        elif n % 5 == 0:
            if n == 5:
                print("este número é primo.")
            else:
                print(f"este número n é primo.")
        else:
            print("este número é primo.")
        pergunta = input("vc deseja ver outro número? ")
        if pergunta != 'sim':
            break

kdena(1)
