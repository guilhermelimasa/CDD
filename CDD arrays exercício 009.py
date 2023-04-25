senha = []
nome = []
for c in range(3):
    nome.append(str(input("digite seu nome: ")))
    senha.append(float(input("digite sua senha: ")))
login_n = str(input("digite seu nome para login: "))
login_s = float(input("digite sua senha para login: "))
for x in range(3):
    if senha[x]==login_s and nome[x]==login_n:
        print("login realizado com sucesso !!!")
