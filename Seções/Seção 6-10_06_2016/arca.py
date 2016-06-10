#-*- encoding=UTF-8 -*-

"""
O Dono do zoológico que fazer uma grande arca e colocar os animais dentro.
Acontece que os animais só podem entrar na arca aos pares. Um número representa
uma espécie. Se esse número for positivo, é um animal macho e se for um número
negativo e um animal fêmea se for um número negativo. Um casal precisa ter um macho
e uma fêmea da mesma espécie.
"""
def e_par (animal1,animal2):
	"""
	>>> e_par(3,-3)
	True
	>>> e_par(1,2)
	False
	"""
	n = animal1
	n1 = animal2
	if animal1 == (animal2*(-1)):
		return True
	else:
		return False
def tem_par (animal,animais):
	"""
	>>> tem_par (1,[0,2,5,-1])
	True
	>>> tem_par (3,[1,-2,5,8])
	False
	"""
	n = animal
	
	for i in animais:
		if e_par (n,i):
			return True
	return False
def arca (animais):
	"""
	>>> arca( [0,1,-1,2,3,5,-6])
	1
	"""
	cont = 1
	pares = 0
	for i in animais:
		subvetor = animais[cont:]
		#print i, subvetor
		if tem_par (i,subvetor):
			pares = pares + 1
		cont = cont + 1
	return pares
		

import pydojo
pydojo.testmod()











