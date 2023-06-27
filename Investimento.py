from abc import ABC
from Cliente import Cliente

class Investimento(ABC):
    def __init__(self, cliente: Cliente, saldo: float = 0.0) -> None:
        super().__init__(cliente, saldo)

    def rendimento(self):
        pass
