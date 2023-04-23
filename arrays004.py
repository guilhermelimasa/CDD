lista = []
listam=[]
x = int(input("digite um número: "))
for c in range(5):
    lista.append(int(input("digite um número: ")))
for y in range(5):
    listam.append(lista[y]*x)
for z in range(5):
    print(listam[z], end=" ")
print('\nCHUVA!!!!!')