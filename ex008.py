def shushana(terraria):
    a = []
    for x in terraria:
        if x not in a:
            a.append(x)
    print(a)

b = [8, 9, 4, 8, 2, 1, 5, 1, 9, 0]

shushana(b)
