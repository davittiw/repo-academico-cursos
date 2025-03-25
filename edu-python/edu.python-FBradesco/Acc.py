class Acc:
    def __init__(self, titular, numero):
        self.titular = titular
        self.numero = numero
        self._saldo = 0

    @property #Somente quando transformado ou verificar atributo (atribuído ou lido)
    def saldo(self):
        return self._saldo

    @saldo.setter #obtendo o valor do atributo set
    def saldo(self, valor):
        if (valor < 0): #se saldo negativo, nao retorna o valor
            print("O saldo não pode ser negativo")
        else:
            self._saldo = valor #saldo positivo, retorna o valor

    def saque(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def deposito(self, valor):
        if (valor > 0):
            self.saldo += valor
            print("Deposito realizado com sucesso")
        else:
            print("Depósito não realizado")

    def extrato(self):
        print("Cliente: ", self.titular, "Saldo atual: ", self.saldo)