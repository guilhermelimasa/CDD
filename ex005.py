pergunta = 's'
while pergunta == 's':
    n1 = float(input("digite sua primeira nota: "))
    while n1 < 0 or n1 > 10:
        n1 = float(input("número errado tente novamente: "))
    n2 = float(input("digite sua segunda nota: "))
    while n2 < 0 or n2 > 10:
        n2 = float(input("numero errado tente novamente: "))
    media = (n1+n2)/2
    print(media)
    pergunta = input("vc deseja fazer um novo cálculo? ")
print("processo finalizado")

