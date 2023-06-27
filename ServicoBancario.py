from Cliente import Cliente
from abc import ABC

class ServicoBancario(ABC):
    numero_contas = 0

    def __init__(self, cliente: Cliente, saldo: float = 0.0) -> None:
        self.__numero = self.gerar_numero()
        self.__titular = cliente
        self.__saldo = saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self) -> float:   # consultar_saldo
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor) -> None:
        self.__saldo = valor

    def consultar_extrato(self):
        pass

    def gerar_numero(self) -> str:
        ServicoBancario.numero_contas += 1
        return ServicoBancario.numero_contas

    def __str__(self) -> str:
        return f"Numero da conta: {self.numero}\nNome do Titular: {self.titular}\nSaldo: {self.saldo}"