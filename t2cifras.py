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

	entrada = raw_input('Informe o arquivo criptografado: \t')
	arquivo = open(entrada,'rb')
	data    = arquivo.readlines()

	global dadosCrypt
	for line in data:
		for c in line:
			dadosCrypt.append(ord(c))

	arquivo.close()
	
def transposicao():
	chave = -1
	
	entrada = raw_input('Informe o arquivo criptografado: \t')
	arquivo = open(entrada,'rb')
	data    = arquivo.readlines()
	lines	= len(data)
	columns = len(data[0])
	for c in data:
		if( columns != len(c)):
			return chave 

	chave = lines
	return chave

def vigenere():
	chave = -1
	return chave

def substituicao():
	chave = -1
	return chave

def caesar():
	readFile()
	chave = ((dadosCrypt[0] + 256) - dadosClear[0]) % 256
	size  = len(dadosClear)
	for c in range(1,size):
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
	chave = caesar()
	if( chave != -1 ):
		print "Caesar \t Chave: " + str(chave)
	chave = transposicao()
	if( chave != -1 ):
		print "Transposicao \t Chave: " + str(chave)



	vigenere()
	substituicao()

		

main()
