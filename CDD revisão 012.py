inicio = int(input("digite a hora de inicio: "))
fim = int(input("digite a hora de fim da partida: "))
contador = 0
for c in range(inicio,fim):
    contador +=1
print(f"{contador},horas")