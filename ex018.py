class Banco:
    def __init__(self, nome, tipo_de_conta, num_da_conta):
        self.tipo_de_conta = tipo_de_conta
        self.nome = nome
        self.num_da_conta = num_da_conta
        self.saldo = 0
        self.status_conta = False
        self.credito = 100
        self.limite = 50

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
        if self.status_conta == False:
            print(f"conta desativada")
        elif saque > self.limite:
            print("vc excedeu o seu limite")

        else:
            if self.saldo <= 0:
                print("sem dinheiro na conta")
            else:
                print(f"vc está sacando {saque}")
                self.saldo = self.saldo - saque


    def verificando(self):
        if self.status_conta == True:
            print(f"{self.nome}, vc tem {self.saldo } R$")
        else:
            print("sua conta está desativada")

    def depositar(self, deposito):
        if self.status_conta == True:
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
p1.sacar(10)
p1.verificando()
p1.depositar(200)
p1.verificando()
#p1.desativar()
p1.sacar(50)
print(vars(p1))


