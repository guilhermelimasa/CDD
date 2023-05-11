def estoque(nome, quantidade, valor):
    return nome, quantidade * valor


total = estoque("fubá", 30, 3.5)
print(f" o produto {total[0]} custa {total[1]} R$")
