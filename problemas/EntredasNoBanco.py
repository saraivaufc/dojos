#-*- encoding=UTF-8 -*-

"""
Todas as vezes que alguém passa na porta do maior banco da cidade de Pirenópolis, 
é gravado em um arquivo de log a data e a hora da abertura da porta. Cada registro no 
arquivo de log possui o seguinte formato: 
	[dd-mm-YYYY H:i:s] - Abertura da Porta OK
O gerente do banco precisa saber quantas pessoas entraram no banco no horário de expediente, 
para isso ele solicitou que você faça um programa que verifique se o registro de entrada 
é válido e se a hora se encontra dentro do intervalo de funcionamento do banco, 
das 10:00:00 até as 16:00:00.
"""

def verificaHora(hora):
	"""
	>>> verificaHora('[02-05-2016 10:10:00] - Abertura da Porta OK')
	True
	>>> verificaHora('[02-05-2016 09:00:00] - Abertura da Porta OK')
	False
	>>> verificaHora('[02-05-2016 16:10:00] - Abertura da Porta OK')
	True
	>>> verificaHora('[02-05-2016 16:00:01] - Abertura da Porta OK')
	True
	>>> verificaHora('[02-05-2016 09:56:59] - Abertura da Porta OK')
	False
	"""
	return False


import pydojo
pydojo.testmod()
