class Banco:
    def __init__(self, nome, tipo_de_conta, num_da_conta):
        self.tipo_de_conta = tipo_de_conta
        self.nome = nome
        self.num_da_conta = num_da_conta
        self.saldo = 40
        self.status_conta = False
        self.credito = 20
        self.limite = 50
    def ativar_credito(self):
        if self.credito == True:
            print("seu crédito já está ativado")
        else:
            self.credito = True
            print("seu crédito está ativado.")
    def desativar_credito(self):
        if self.credito == False:
            print("seu crédito já está desativado")
        else:
            self.credito = False
            print("seu crédito está desativado")
    def ativar_limite(self):
        if self.limite == True:
            print("seu limite está ativo.")
        else:
            self.limite = True
            print("seu limite está ativo")
    def desativar_limite(self):
        if self.limite == False:
            print("seu limite já está desativado.")
        else:
            self.limite = False
            print("seu limite está desativado.")
    def ativar(self):
        if self.status_conta == True:
            print("sua conta já está ativada")
        else:
            self.status_conta = True
        print("sua conta foi ativada.")
    def sacar(self, saque):
        print(f"vc está sacando {saque}")
        if self.status_conta == False:
            print(f"conta desativada")
        elif self.limite == True:
            if saque > self.limite:
                print(f"vc tentou sacar R${saque} infelizmente o seu limite é de R${self.limite}")
        else:
            if self.saldo <= 0:
                print("sem dinheiro na conta")
            else:
                if self.saldo < saque:
                    self.credito = self.saldo + self.credito - saque
                    self.credito = self.credito - (self.credito * 2) - 9
                    self.saldo = 0
                else:
                    print(f"vc está sacando {saque}")
                    self.saldo = self.saldo - saque

    def verificando(self):
        if self.status_conta == True:
            print(f"{self.nome}, vc tem R${self.saldo } de saldo e R${self.credito} de crédito ")
        elif self.credito < 100:
            print(f"{self.nome} vc tem que pagar {100-self.credito} para quitar suas dívidas.")
        else:
            print("sua conta está desativada")
    def depositar(self, deposito):
        if self.status_conta == True:
            if self.credito < 100:
                print("vc tem que quitar suas dívidas de crédito")
                self.saldo = deposito - self.credito
                self.credito = 100
            else:
                print(f"vc está depositanto {deposito}")
                self.saldo = self.saldo + deposito
        else:
            print("sua conta está desativada")
    def desativar(self):
        if self.status_conta == False:
            print("sua conta já está desativada")
        else:
            if self.saldo > 0:
                print("vc precisa retirar todo o seu dinheiro.")
                self.saldo = 0
                print(f"{self.nome}, seu saldo é {self.saldo}")
            self.status_conta = False
        print("sua conta foi desativada")








p1 = Banco ("Guilherme", "corrente", 89012364789)
p1.ativar()
#p1.ativar_limite()
#p1.verificando()
p1.ativar_credito()
p1.sacar(50)
p1.verificando()
#p1.depositar(200)
#p1.verificando()
#p1.desativar()
#print(vars(p1))
#p1.desativar_limite()
#p1.desativar_credito()


