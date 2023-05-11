
def somar(*zedamanga):
    soma = 0
    for c in range(len(zedamanga)):
        soma = zedamanga[c] + soma
    return soma

print(somar(2,3))
