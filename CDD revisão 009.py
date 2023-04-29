ano = float(input("quantos anos vc tem ? "))
mes = float(input("e quantos meses? "))
dias = float(input("e quantos dias? "))
idade_1 = ano * 360
idade_2 = mes * 30
idade = idade_1 + idade_2 + dias
print(f"vc viveu aproximadamente {idade} dias")
