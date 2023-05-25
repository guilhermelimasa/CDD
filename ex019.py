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
        print(f"{self.nome} está miando.")

    def comendo(self, comida):
        print(f"{self.nome} está commendo {comida}")


p1 = gato('jujuba', 'malhado')
p1.emitir_som()
p1.comendo("ração")


class coelho(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def pular(self):
        print(f"{self.nome} está pulando")

    def comendo(self, comida):
        print(f"{self.nome} está comendo {comida}")


p2 = coelho('chão', 'branco')
p2.pular()
p2.comendo("cenoura")


class vaca(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f"{self.nome} está mugindo")

    def comendo(self, comida):
        print(f"{self.nome} está comendo {comida}")


p3 = vaca('jassinta', 'amarela')
p3.mugir()
p3.comendo("grama")
