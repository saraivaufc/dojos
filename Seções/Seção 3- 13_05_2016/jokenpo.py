#-*- encoding=UTF-8 -*-

def juiz(jogador1, jogador2):
	"""
	>>> juiz('Pedra', 'Pedra')
	'Empate'
	>>> juiz('Pedra', 'Tesoura')
	'Ganhasds'
	>>> juiz('Tesoura', 'Tesoura')
	'Empate'
	>>> juiz('Tesoura', 'Papel')
	'Ganha'
	>>> juiz('Tesoura', 'Pedra')
	'Perde'
	"""
	return 'Casa'
	
import pydojo
pydojo.testmod()

