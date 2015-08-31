dadosCrypt = []

def readFile():
	entrada = raw_input('Informe o arquivo criptografado: \t')
	arquivo = open(entrada,'rb')
	data    = arquivo.readlines()

	global dadosCrypt
	for line in data:
		for c in line:
			dadosCrypt.append(ord(c))

	arquivo.close()

def carregaDicionarios():
	''' carrega os dicionarios portugues, latim e ingles '''
	