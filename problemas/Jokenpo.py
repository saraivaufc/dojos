#-*- encoding=UTF-8 -*-

"""
Jokenpo é uma brincadeira japonesa, onde dois jogadores escolhem um  dentre três 
possíveis itens: Pedra, Papel ou Tesoura. O objetivo é fazer um juiz de Jokenpo 
que dada a jogada dos dois jogadores informa o resultado da partida.
As regras são as seguintes:
	Pedra empata com Pedra e ganha de Tesoura
	Tesoura empata com Tesoura e ganha de Papel
	Papel empata com Papel e ganha de Pedra
	Os únicos resultados possíveis são: Ganha   #caso o jogador 1 ganhe do jogador 2
										Perde   #caso o jogador 1 perda para o jogador 2
										Empate  #caso os dois façam a mesma jogada
"""

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

