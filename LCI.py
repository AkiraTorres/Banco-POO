from Cliente import Cliente
from Investimento import Investimento

class LCI(Investimento):
    def __init__(self, cliente: Cliente, saldo: float = 0.0) -> None:
        super().__init__(cliente, saldo)
        