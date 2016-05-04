#-*- encoding=UTF-8 -*-


#Para saber se um número é feliz, você deve obter o quadrado de cada 
#dígito deste número, em seguida você faz a soma desses resultados. 
#A seguir o mesmo procedimento deve ser feito com o valor resultante desta soma. 
#Se ao repetir o procedimento diversas vezes obtivermos o valor 1, o número inicial 
#é considerado feliz.
#Tomamos o 7, que é um número feliz:
#7² = 49
#4² + 9² = 97
#9² + 7² = 130
#1² + 3² + 0² = 10
#1² + 0² = 1
#Podemos observar nesse exemplo que os números 49, 97, 130 e 10 também são felizes. 
#Existem infinitos números felizes.
#Desenvolva um programa que determine se um número é feliz ou triste.

def retornaDigitos(numero):
	"""
	>>> retornaDigitos(2)
	[2]
	>>> retornaDigitos(21)
	[2, 1]
	>>> retornaDigitos(122342323)
	[1, 2, 2, 3, 4, 2, 3, 2, 3]
	"""
	lista = []
	while numero>=10:
		x = numero%10;
		numero = numero/10;
		lista.append(x)
	lista.append(numero)
	lista.reverse()
	return lista

def eFeliz(numero, vezes):
	"""
	>>> eFeliz(7, 100)
	True
	>>> eFeliz(2, 100)
	False
	>>> eFeliz(3, 100)
	True
	>>> eFeliz(4, 100)
	True
	>>> eFeliz(49, 100)
	True
	>>> eFeliz(97, 100)
	True
	>>> eFeliz(130, 100)
	True
	"""
	for  i in range(0,vezes):
		val = 0
		for k in retornaDigitos(numero):
			val += pow(k,2)
		if val == 1:
			return True
		else:
			numero = val;
		print val
	return False

def imprimeFelizes(n):
	print [x for x in range(0,n) if eFeliz(x, 20)]
	


import pydojo
pydojo.testmod()
