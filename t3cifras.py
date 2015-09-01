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



def main():
	readFile()

	chave = caesar()
	if( chave != -1 ):
		print "Caesar \t Chave: " + str(chave)
	chave = transposicao()
	if( chave != -1 ):
		print "Transposicao \t Chave: " + str(chave)
	chave =  vigenere()
	if( len(chave) > 0):
		print "Vigenere"
	chave = substituicao()
	if( len(chave) > 0):
		print "Substituicao"


	