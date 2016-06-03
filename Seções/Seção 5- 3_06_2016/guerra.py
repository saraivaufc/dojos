def guerra (soldados):
	"""
	>>> guerra([1, 1.25, 1.75])
	'1,1.25-1.75'
	
	"""
	soma = 0
	cont = 0
	for elem in soldados:
		soma = soma + elem
		cont = cont + 1
	media = soma /cont
	grande = ""
	pequeno = ""
	eh_primeiro  = 1
	eh_primeiro2 = 1
	for i in soldados:
		if i >= media:
			if eh_primeiro2 == True:
				
				grande = grande + str(i)
				eh_primeiro2 = False
			else:
				grande = grande + "," + str(i)
		else:
			if eh_primeiro == True:
				
				pequeno = pequeno + str(i)
				eh_primeiro = False
			else:
				pequeno = pequeno + "," + str(i)
	return pequeno + "-" + grande












import pydojo
pydojo.testmod()


