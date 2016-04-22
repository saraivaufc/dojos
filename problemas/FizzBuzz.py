#-*- encoding=utf-8 -*-

"""
FizzBuzz
Neste problema, você deverá retornar uma palavra de acordo com a entrada, seguindo as
seguinte regras:
Se entrada for um número divisíveil por 3, a função deve retornar 'Fizz';
Se entrada for um número divisíveil por 5, a função deve retornar 'Buzz';
Se entrada for um número divisíveil por 3 e 5 simultaneamente, a função deve retornar 'FizzBuzz';
Se não for nenhua das opções abaixo, a função deverá retornar o próprio número.
"""


def fizzBuzz(numero):
	"""
	>>> fizzBuzz(1)
	1
	>>> fizzBuzz(3)
	'Fizz'
	>>> fizzBuzz(5)
	'Buzz'
	>>> fizzBuzz(12)
	'Fizz'
	>>> fizzBuzz(15)
	'FizzBuzz'
	"""
	
	if numero % 3 == 0 and numero % 5 == 0:
		return 'FizzBuzz'
	if numero % 3 == 0:
		return 'Fizz'
	if numero % 5 == 0:
		return 'Buzz'
	return numero
	


import pydojo
pydojo.testmod()
