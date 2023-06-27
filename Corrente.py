from ServicoBancario import ServicoBancario
from Cliente import Cliente


class Corrente(ServicoBancario):
    def __init__(self, cliente: Cliente, saldo: float = 0.0) -> None:
        super().__init__(cliente, saldo)

    def deposito(self, valor: float) -> None:
        if valor > 0:
            self.saldo += valor

    def saque(self, valor: float) -> None:
        if valor <= 0 and self.saldo < valor:
            raise Exception("Não foi possível realizar essa transferência.")
            return
        self.saldo -= valor

    def transferencia(self, valor: float, destinatario: ServicoBancario) -> None:
        self.saque(valor)
        destinatario.saldo += valor
