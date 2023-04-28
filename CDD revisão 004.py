list = []
maior = 0
numero = 0
x = int(input("quantos números vão ser: "))
for z in range(x):
    list.append(float(input("digite um número: ")))
    if numero == 0:
     maior = list[z]
     menor = list[z]
    numero = 1
    if list[z] > maior:
        maior = list[z]
print(f"o maior número é: {maior}")

#c = float(input("digite um número: "))
#y = float(input("digite um segundo número: "))
#x = float(input("digite um terceiro valor: "))
#if c > y:
    #if c> x:
        #print(f"{c}é o maior número.")
    #else:
        #print(f"{x} é o maior número.")
#elif y > c:
    #if y > x:
        #print(f"{y} é o maior número.")
    #else:
        #print(f"{x} é o maior número.")

