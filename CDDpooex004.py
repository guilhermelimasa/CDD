class forma:
    def __init__(self, area, perimetro):
        self.area = area
        self.perimetro = perimetro

class triangulo(forma):
    def __init__(self, area, perimetro, altura):
        self.altura = altura
        super().__init__(area, perimetro)


    def calcular_area(self,b):
        area = (b * self.altura) / 2
        print(f"a área do triângulo é {area}")

    def calcular_perimetro(self, l1, l2, l3):
        print(f"o perímetro desse triângulo é {l1 +  l2 + l3}")

class retangulo(forma):
    def __init__(self, area, perimetro):
        super().__init__(area, perimetro)


    def calcular_area(self,ba,al):
        print(f"a área desse retângulo é {ba * al}")


    def calcular_perimetro(self,l,l1):
        print(f"o perimêtro desse retângulo é {(l * 2) + (l1 * 2)}")

p1 = triangulo(10, 2, 4)
p1.calcular_area(7)
p1.calcular_perimetro(7, 8, 9)
p2 = retangulo(0, 0)
p2.calcular_area(10, 12)
p2.calcular_perimetro(10, 12)

