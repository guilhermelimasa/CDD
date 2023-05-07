nome = []
senha = []
for c in range(5):
    nome.append(str(input("digite seu nome: ")))
    senha.append(int(input("digite sua senha: ")))
for x in range(5):
    login_n = input("digite o seu nome: ")
    login_s = int(input("digite sua senha: "))
    if login_n in nome and login_s in senha:
        print("bem vindo")
    else:
        print("usuário ou senha incorreto!!")
print("programa encerrado!!!")
