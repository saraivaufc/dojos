def soma(numero1, numero2):
    """
    >>> soma(2,3)
    5
    >>> soma(-1, 4)
    3
    """
    return numero1 + numero2

class Calculadora():
    def soma(self, numero1, numero2):
        """
        >>> calculadora = Calculadora()
        >>> calculadora.soma(1,2)
        3
        >>> calculadora.soma(4,8)
        12
        >>> calculadora.soma(-1,3)
        2
        """
        return numero1 + numero2

import pydojo
pydojo.testmod()
