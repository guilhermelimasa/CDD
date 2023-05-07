nome = []
senha = []
for c in range(5):
    nome.append(str(input("digite seu nome: ")))
    senha.append(int(input("digite sua senha: ")))
for x in range(5):
    print(f"{nome[x]},{senha[x]}-{x+1}")
