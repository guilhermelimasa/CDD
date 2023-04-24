n1 = int(input("digite um número: "))
n2 = int(input("digite outro número: "))
while n2 == 0:
    n2=int(input("digite um número diferente de zero: "))
div = n1 / n2
print(f"a divisão é {div}")