class atleta:
    def __init__(self, aposentado, peso, aquece):
        self.aposentado = False
        self.peso = False
        self.aquece = False
    def aposentar(self):
        if self.aposentado == True:
            print("vc já está aposentado")
        else:
            self.aposentado = True
            print("agora vc está aposentado")

    def aquecer(self):
        if self.aquece == True:
            print("vc já está aquecido")
        else:
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
        self.p = False
    def pedalar(self):
        if self.aposentado == True:
            print("vc está aposentado, não pode mais pedalar.")
        else:
            if self.aquece == True:
                print("vc está pedalando.")
                self.p = True
            else:
                print("vc não pode pedalar pois não está aquecido.")

class corredor(atleta,nadador,ciclista):
    def __init__(self, aposentado, peso, aquece):
        super(). __init__(aposentado, peso, aquece)
        self.c = False

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
        self.correr = False
        self.nadar = False
        self.pedalar = False

    def correr(self):
        if self.aposentado == True:
            print("vc não pode correr pois está aposentado.")
        else:
            if self.aquece == False:
                print("vc não pode correr pois não está aquecido")
            else:
                if self.nadar == True:
                    print("vc não pode correr pois está nadando")
                elif self.pedalar == True:
                    print("vc não pode correr pois está pedalando")
                else:
                    self.correr = True
                    print("vc está correndo.")




    def nadar(self):
        if self.aposentado == True:
            print("vc não pode nadar pois está aposentado.")
        else:
            if self.aquece == False:
                print("vc não pode nadar pois não está aquecido")
            else:
                if self.correr == True:
                    print("vc não pode nadar pois está correndo.")
                elif self.pedalar == True:
                    print("vc nao pode nadar pois está pedalando")
                else:
                    self.nadar = True
                    print("vc está nadando")


    def pedalar(self):
        if self.aposentado == True:
            print("vc não pode pedalar pois está aposentado")
        else:
            if self.aquece == False:
                print("vc não pode pedalar pois não está aquecido")
            else:
                if self.correr == True:
                    print("vc não pode pedalar pois está correndo.")
                elif self.nadar == True:
                    print("vc não pode pedalar pois está nadando.")
                else:
                    self.pedalar = True
                    print("vc está pedalando")



    def parardecorrer(self):
        if self.correr == False:
            print("vc não está correndo, não pode parar de correr")
        else:
            self.correr = False
            print("vc parou de correr")

    def parardenadar(self):
        if self.nadar == False:
            print("vc não está nadando, logo não pode parar de nadar")
        else:
            self.nadar = False
            print("vc parou de nadar")

    def parardepedalar(self):
        if self.pedalar == False:
            print("vc não está pedalando, logo não pode parar de pedalar")
        else:
            self.pedalar = False
            print("vc parou de pedalar")


p1 = triatleta(" ", " ", " ")
p1.aquece()
