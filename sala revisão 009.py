pessoas = int(input("digite o total de eleitores: "))
votos_brancos = int(input("digite o número de votos  brancos: "))
votos_nulos = int(input("digite o número de votos válidos: "))
votos_validos = int(input("digite o número de votos válidos: "))
brancos = (votos_brancos*100)/pessoas
nulos = (votos_nulos*100)/pessoas
validos = (votos_validos*100)/pessoas
print(f"a porcentagem de brancos foi {brancos:.2f}%, a de nulos foi {nulos:.2f}%, e a de válidos foi {validos:.2f}%.o total de pessoas é {pessoas:.2f}")
