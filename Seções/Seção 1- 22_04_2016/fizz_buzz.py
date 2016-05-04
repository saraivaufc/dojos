#-*- encoding=utf-8 -*-

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
