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
	if jogador1 == jogador2:
		return 'Empate'
	elif jogador1 == 'Pedra':
		if jogador2 == 'Tesoura':
			return 'Ganha'
		else:
			return 'Perde'
	elif jogador1 == 'Tesoura':
		if jogador2 == 'Papel':
			return 'Ganha'
		else:
			return 'Perde'
	elif jogador1 == 'Papel':
		if jogador2 == 'Pedra':
			return 'Ganha'
		else:
			return 'Perde'
	
	
import pydojo
pydojo.testmod()

