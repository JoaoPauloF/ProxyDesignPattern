"""
Proxy 
	Prove um meio de acesso para outro objeto acessa-lo atraves do mesmo.
"""

import abc


class Assunto(metaclass=abc.ABCMeta):
    """
    Define uma interface comum entre o AssuntoVerdadeiro e o Proxy 
    para que um Proxy possa ser usado em qualquer lugar onde um AssuntoVerdadeiro
    e esperado
    """

    @abc.abstractmethod
    def request(self):
        pass


class Proxy(Assunto):
    """
    Mantem uma referencia que permite que o proxy acesse o assunto verdadeiro
    Prove uma interface identica a do assunto.
    """

    def __init__(self, assunto_verdadeiro):
        self._assunto_verdadeiro = assunto_verdadeiro

    def request(self):
        # ...
        self._assunto_verdadeiro.request()
        # ...


class AssuntoVerdadeiro(Assunto):
    """
    Define um objeto real que o proxu ira representar
    ""

    def request(self):
        pass


def main():
    assunto_verdadeiro = AssuntoVerdadeiro()
    proxy = Proxy(assunto_verdadeiro)
    proxy.request()


if __name__ == "__main__":
    main()
