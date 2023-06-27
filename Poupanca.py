from Investimento import Investimento
from Cliente import Cliente


class Poupanca(Investimento):
    def __init__(self, cliente: Cliente, saldo: float = 0.0) -> None:
        super().__init__(cliente, saldo)

    def aplicacao(self):
        pass
