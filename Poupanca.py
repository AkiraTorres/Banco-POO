from Banco.LCI import LCI
from Banco.Cliente import Cliente


class Poupanca(LCI):
    def __init__(self, num: str, cliente: Cliente) -> None:
        super().__init__(num, cliente)

    def aplicacao(self):
        pass
