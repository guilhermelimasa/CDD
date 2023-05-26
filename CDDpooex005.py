class atleta:
    def __init__(self, aposentado, peso, aquece):
        self.aposentado = False
        self.peso = False
        self.aquece = False
    def aposentar(self):
        self.aposentado = True
        print("agora vc está aposentado")

    def aquecer(self):
        self.aquece = True
        print("vc está aquecido.")


class nadador(atleta):
    def __init__(self, aposentado, peso, aquece):
        super().__init__(aposentado, peso, aquece)


    def nadar(self):
       if self.aposentado == True:
           print("vc não pode nadar, pois está aposentado")
       else:
            if self.aquece == True:
                print("o nadador está nadando")
            else:
                print("o nadador não está aquecido, ent não pode nadar")

class ciclista(atleta):
    def __init__(self, aposentado, peso, aquece):
        super(). __init__(aposentado, peso, aquece)

    def pedalar(self):
        if self.aposentado == True:
            print("vc está aposentado, não pode mais pedalar.")
        else:
            if self.aquece == True:
                print("vc está pedalando.")
            else:
                print("vc não pode pedalar pois não está aquecido.")

class corredor(atleta):
    def __init__(self, aposentado, peso, aquece):
        super(). __init__(aposentado, peso, aquece)

    def correr(self):
        if self.aposentado == True:
            print("vc está aposentado, não pode mais correr.")
        else:
            if self.aquece == True:
                print("vc está correndo.")
            else:
                print("vc não pode correr pois não está aquecido.")

class triatleta(corredor, ciclista, nadador):
    def __init__(self, aposentado, peso, aquece):
        super(). __init__(aposentado, peso, aquece)



p1 = triatleta(" ", " ", " ")
p1.aposentar()
p1.aquecer()
p1.correr()
p1.pedalar()
p1.nadar()
