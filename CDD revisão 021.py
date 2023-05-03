x = float(input("digite um número: "))
y = float(input("digite outro número: "))
if y == 0:
    while y == 0:
        y = float(input("digite um valor diferente de zero: "))
div = x / y
print(f"a divisão de {x} por {y} é {div}.")
