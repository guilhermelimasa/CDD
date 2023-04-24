for x in range(0, 10):
    x = x + 1
    print(x, end=" ")
print("   agora decrescente: ")
for x in range(10, 0, -1):
    print(x, end=" ")

print("   agora usando while: ")
contador = 0
while contador != 10:
    contador += 1
    print(contador, end=" ")
print("   agora decrescente usando while: ")
contador = 11
while contador != 1:
    contador -= 1
    print(contador, end=" ")
