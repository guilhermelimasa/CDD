class Pessoa:
    def __init__(self, nome, peso, idade, comendo=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo

    def comer(self, comida):
        self.comida = comida
        if self.comendo == False:
            print(f"{self.nome} está comendo {self.comida}")
            self.comendo = True
        else:
            print(f"{self.nome} já está comendo.")

    def para_de_comer(self):
        if self.comendo == False:
            print(f"{self.nome} não está comendo.")
        else:
            print(f"{self.nome} parou de comer")
            self.comendo=False

    def falar(self, falar):
        self.falar = falar
        if self.comendo == False:
            print(f"{self.nome} não pode falar pois está comendo")
        else:
            print(f"{self.nome} está falando")
            self.falar = True
    def parar_de_falar(self):
        if self.falar == False:
            print(f"{self.nome} parou de falar")
        else:
            print(f"{self.nome} parou de falar")
    def andar(self,andar):
        self.andar = andar
        if self.comendo == False:
            print(f"{self.nome}está comendo e andando")
            self.andar = True
        elif self.comendo == True:
            print(f"{self.nome}está andando")
            self.andar = True
        elif self.falar == True:
            print(f"{self.nome}está andando e falando")
            self.andar = True
        elif self.falar == False:
            print(f"{self.nome}está andando")
            self.andar = True
    def parar_de_andar(self):
        if self.andar == True:
            print(f"{self.nome} parou de andar")


p1 = Pessoa("Guilherme", 80, 19)
p1.comer(input(("o que vc está comendo? ")))
p1.comer("manteiga")
p1.para_de_comer()
p1.falar()
p1.parar_de_falar()
p1.andar()
p1.parar_de_andar()
