from Cliente import Cliente
from Corrente import Corrente
from ServicoBancario import ServicoBancario

def main():
    cliente1 = Cliente('12345678900', 'Torres', '05-05-2001')
    corrente1 = Corrente(cliente1, 430)

    cliente2 = Cliente("98765432100", "Julio", "17-07-2004")
    corrente2 = Corrente(cliente2)

    corrente1.transferencia(49.90, corrente2)

    x = ServicoBancario(cliente1, 430)

    print(corrente1)
    print()
    print(corrente2)
    print(x)


if __name__ == '__main__':
    main()