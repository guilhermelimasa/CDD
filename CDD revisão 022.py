n1 = float(input("Digite a primeira nota: "))
while n1 < 0 or n1 > 10:
    n1 = float(input("digite um novo valor para a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
while n2 < 0 or n2 > 10:
    n2 = float(input("digite um novo valor para a segunda nota: "))
media = (n1+n2)/2
print(media)


