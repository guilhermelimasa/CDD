senhacorreta = "banana"
contador = 1
senha = input("digite sua senha: ")
while senhacorreta != senha:
    contador = contador + 1
    print("senha incorreta tente novamente: ")
    senha = input
    if contador>2 and senha != senhacorreta:
        print("senha bloqueada ")
        break


else:
    print("BEM VINDO!!!")