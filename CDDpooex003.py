class animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def comer(self):
        print(f"{self.nome} está comendo.")
class gato(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitir_som(self):
        print(f"{self.nome} está miando")

    def comendo(self, comida):
        print(f"{self.nome} está comendo {comida}")

class cachorro(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def som(self):
        print(f"{self.nome} está latindo")
    def comendo(self,comida):
        print(f"{self.nome} está comendo {comida}")


p2 = cachorro("totó", "branco")
p2.som()
p2.comendo("manga")
p1 = gato("marrie", "branca e preto")
p1.emitir_som()
p1.comendo('banana')
