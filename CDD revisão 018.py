a = []
b = []
c = []
n = int(input("digite um número: "))
for x in range(n):
    a.append(int(input("digite um número para a lista A: ")))
    b.append(int(input("digite um número para a lista B: ")))
for y in range(n):
    c.append(a[y]+b[y])
print(f"a soma das duas listas fica {c}")
if c[-1] % 2 != 0:
    for r in range(n):
        if c[r] % 2 == 0:
            print(f"o número par é {c[r]}")
c = []
for v in range(n):
    c.append(a[v]-b[v])
print(f"a subtração das duas listas fica {c}")
c = []
for h in range(n):
    c.append(a[h]*b[h])
print(f"a multiplicação das duas listas fica{c}")
c = []
print(f"a lista C vazia fica {c}")
