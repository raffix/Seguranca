dadosClear = []
dadosCrypt = []

def readFile():
	entrada = raw_input('Informe o arquivo de claro: \t')
	arquivo = open(entrada,'rb')
	data    = arquivo.readlines()

	global dadosClear
	for line in data:
		for c in line:
			dadosClear.append(ord(c))

	arquivo.close()

	entrada = raw_input('Inform o arquivo criptografado: \t')
	arquivo = open(entrada,'rb')
	data    = arquivo.readlines()

	global dadosCrypt
	for line in data:
		for c in line:
			dadosCrypt.append(ord(c))

	arquivo.close()
	
def transposicao():

def vigenere():

def substituicao():

def caesar():
	readFile()
	chave = ((dadosCrypt[0] + 256) - dadosClear[0]) % 256
	for c in range(1,len(dadosClear))
		temp = ((dadosCrypt[c] + 256) - dadosClear[c]) % 256
		if( chave != temp):
			return -1

	arquivo = open("saida/t2CaesarDescriptografado",'wb')
	for c in dadosCrypt:
		temp = ((c + 256) - chave ) % 256 
		arquivo.write(chr(temp))
		
	arquivo.close()
	return chave



def main():

	if( (chave = ceasar()) != -1 ):
		print "Caesar \t Chave: " + str(chave)
	if( (chave = transposicao()) != -1 ):
		print "Transposicao \t Chave: " + str(chave)

	vigenere()
	substituicao()

		

main()
