##Repositório dos PyDojos UFC
####Esse é o repositório das ferramentas e problemas utilizados nas reuniões dos dojos de programação em python que ocorrem na Universidade Federal do Ceará - Campus Quixadá.

#####Para utilizar a biblioteca de testes pydojo.py, basta seguir os seguintes comandos:
1) Baixar o arquivo pydojo.py no mesmo diretório onde se encontra o arquivo que será aplicado os testes.
</br>
2) Para criar os casos de testes, basta adicionar, após a definição da função, uma string com todos os casos de testes, veja seguir:
</br>
Para funções:
```python

    def soma(numero1, numero2):
        """
        >>> soma(1,2)
        3
        >>> soma(4,8)
        12
        >>> soma(-1, 3)
        2
        """
    return numero1 + numero2
```
</br>
Para metodos de classes:
```python
    class Calculadora():
        def soma(self, numero1, numero2):
            """
            >>> calculadora = Calculadora() #basta criar o objeto uma única vez.
            >>> calculadora.soma(1,2)
            3
            >>> calculadora.soma(4,8)
            12
            >>> calculadora.soma(-1,3)
            2
            """
            return numero1 + numero2
```
3) Após todos os casos de testes adicionados, é nescessário executar os testes com a ajuda do pydojo.py:
```python
      import pydojo
      pydojo.testmod()
```
4) Veja o código completo:
```python
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
```
