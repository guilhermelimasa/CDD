x = int(input("digite um número: "))
y = int(input("digite outro número: "))
z = int(input("digite mais um número: "))
if x > y:
    if x > z:
        print(f"{x} é o maior número.")
    else:
        print(f"{z} é o maior número.")
elif y > x:
    if y > z:
        print(f"{y} é o maior número.")
    else:
        print(f"{z} é o maior número.")

