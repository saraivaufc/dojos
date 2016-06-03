def ru (numero,fila):
	"""
	>>> ru(5,[1,2,3,4,5])
	'135-24'
	"""
	alunos = ""
	stas = ""
	for elem in fila:
		if elem%2!=0:
			alunos = alunos + str(elem)
		else:
			stas = stas + str(elem)
		
	return alunos + "-" + stas
import pydojo
pydojo.testmod()

