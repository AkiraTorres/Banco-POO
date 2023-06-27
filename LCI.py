from Banco.ServicoBancario import ServicoBancario
from Banco.Cliente import Cliente


class LCI(ServicoBancario):
    def __init__(self, num: str, cliente: Cliente) -> None:
        super().__init__(num, cliente)

    def rendimento(self):
        pass
