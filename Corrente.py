from Banco.ServicoBancario import ServicoBancario
from Banco.Cliente import Cliente


class Corrente(ServicoBancario):
    def __init__(self, num: str, cliente: Cliente) -> None:
        super.__init__(num, cliente)

    def deposito(self, valor: float) -> None:
        if valor > 0:
            self.saldo += valor

    def saque(self, valor: float) -> None:
        if valor <= 0 and self.saldo < valor:
            raise Exception("Não foi possível realizar essa transferência.")
            return
        self.saldo -= valor

    def transferencia(self, valor: float, destinatario: ServicoBancario) -> None:
        try:
            self.saque(valor)
        except Exception:
            print(Exception.with_traceback)
            return
        destinatario.saldo += valor
