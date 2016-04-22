#-*- encoding=UTF-8 -*-

"""
Desenvolver um programa no qual o usuário entra com a sua idade e, dependendo dela, é classificado em uma categoria 
(criança, adolescente, adulto, idoso).
"""
def idade (numero):
	"""
	>>> idade(3)
	'Crianca'
	>>> idade(67)
	'Idoso'
	>>> idade(18)
	'Adulto'
	>>> idade(13)
	'Adolescente'
	"""
	if numero>=0 and numero<=12:
		return 'Crianca'
	elif numero>=13 and numero<=17:
		return 'Adolescente'
	elif numero>=18 and numero<=59:
		return 'Adulto'
	return 'Idoso'
import pydojo
pydojo.testmod()


