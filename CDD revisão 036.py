Eleitores = int(input('digite o número de eleitores: '))
votos_brancos = int(input('digite o número de votos em branco: '))

while votos_brancos > Eleitores:
    votos_brancos = int(input('Informe um número válido de votos em branco.'))
contagem_nulo_v = Eleitores-votos_brancos

print(f'Restam {contagem_nulo_v} votos')

if votos_brancos != Eleitores:
    votos_n = int(input('digite o número de votos Nulos: '))

    while votos_n > contagem_nulo_v:
        votos_n = int(input('informe um número válido de votos em nulo: '))
    contagem_nulo_v = contagem_nulo_v-votos_n

    print(f'Restam {contagem_nulo_v} votos')
    votos_validos = contagem_nulo_v
else:
    votos_n = contagem_nulo_v
    votos_validos = contagem_nulo_v

pvb = 100*votos_brancos/Eleitores
pvn = 100*votos_n/Eleitores
pvv = 100*votos_validos/Eleitores

print('-------')
print(f'O de votos brancos é: {pvb:.2f}%')
print(f'O número de votos nulos é: {pvn:.2f}%')
print(f'O número de votos validos é: {pvv:.2f}%')
