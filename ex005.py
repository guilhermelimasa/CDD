def somar(n1,n2):
    print(f"a soma dos números é: {n1+n2}")
def subtrair(n1, n2):
    print(f"a subtração dos números é: {n1-n2}")
def multiplicar(n1,n2):
    print(f"a multiplicação dos números é: {n1*n2}")
def dividir(n1,n2):
    print(f"a divisão do primeiro pelo segundo é {n1/n2}")
n1 = 0
n2 = 0
while True:
    pergunta = input(""" Qual operação vc deseja:
    1- somar
    2- subtrair
    3- multiplicar
    4- dividir
    5- sair
     """)
    if pergunta == '5':
        break
    if pergunta != '5':
        n1 = int(input("digite o primeiro número: "))
        n2 = int(input("digite o segundo número: "))
    if pergunta == '1':
        somar(n1, n2)
    if pergunta == '2':
        subtrair(n1, n2)
    if pergunta == '3':
        multiplicar(n1, n2)
    if pergunta == '4':
        dividir(n1, n2)
