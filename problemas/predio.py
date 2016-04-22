#-*- encoding=UTF-8 -*-

"""
Criar um programa que, ao receber o número de andares de um prédio e a altura de cada andar, mostre a altura total do prédio.
"""
def alt_total (andares, altura):
	"""
	>>> alt_total(2,3)
	6
	>>> alt_total(5,4)
	20
	>>> alt_total(7,4)
	28
	"""
	r=andares*altura
	return r
import pydojo
pydojo.testmod()


