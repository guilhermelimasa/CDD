nome = input("Digite um nome: ")
tamanho = 0
#while nome[tamanho:tamanho+1] != "":
    #tamanho += 1
#print(f"O nome {nome} tem {tamanho} letras.")
for c in nome:
    tamanho += 1
print(f"o nome {nome} tem {tamanho} letras.")
