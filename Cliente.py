class Cliente:
    def __init__(self, cpf: str, nome: str, data_nasc: str) -> None:
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nasc = data_nasc

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf: str) -> None:
        self.__cpf = novo_cpf

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str) -> None:
        self.__nome = novo_nome
        
    @property
    def data_nasc(self) -> str:
        return self.__data_nasc
        
    @data_nasc.setter
    def data_nasc(self, novo_data_nasc: str) -> None:
        self.__data_nasc = novo_data_nasc


    def __str__(self) -> str:
        return "{ " + f"Nome: {self.nome} | CPF: {self.cpf} | Nascimento: {self.data_nasc}" + " }"