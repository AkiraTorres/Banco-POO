from Banco.Cliente import Cliente


class ServicoBancario:
    def __init__(self, num: str, cliente: Cliente) -> None:
        numero = num
        titular = cliente
        saldo = 0.0

    def consultarSaldo(self) -> float:
        return self.saldo

    def consultarExtrato(self):
        pass
