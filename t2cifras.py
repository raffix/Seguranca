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



def comparar(decodificacao):
	for c in range(0,len(dadosClear)):
		if( decodificacao[c] != dadosClear[c]):
			return -1
	return 0



def transposicao():
	chave = -1
	size  = len(dadosCrypt)
	c 	  = size
	while c < size:
		temp = size % c 
		if( temp == 0):
			''' Testa para ver se esta chave funciona realmente '''
			colunas    = len(dadosCrypt) / c
			posicao    = 0
			matrizCryp = []
			for d in range(0,c):
				line = []
				for e in range(0,colunas):
					line.append(dadosCrypt[posicao])
					posicao =  posicao + 1
				matrizCryp.append(line)
			decodificacao = []
			for d in (0,colunas):
				for e in (0,c):
					decodificacao.append(e)

			teste = -1
			teste = comparar(decodificacao)
			if( teste == 0 ):
				arquivo = open('saida/t2TransposicaoDecodificado.txt','wb')
				for d in decodificacao:
					arquivo.write(d)
				arquivo.close()
				return c
		c =  c + 1
	return chave



def vigenere():
	chave = []
	for c in range(0,len(dadosCrypt)):
		temp = ((dadosCrypt[c] + 256) - dadosClear[c]) % 256

		chave.append(chr(temp))
	arquivo = open('saida/vigenereChave.txt','wb')
	for c in chave:
		arquivo.write(c)
	arquivo.close()

	chave = map(ord,chave)
	arquivo = open('saida/t2VigenereDescriptografado.txt','wb')
	for c in range(0,len(dadosCrypt)):
		temp = ((dadosCrypt[c] + 256) - chave[c]) % 256
		arquivo.write(chr(temp))
	arquivo.close()
	return chave



def substituicao():
	chave = []
	for c in range(0,255):
		chave.append(0)
	size  = len(dadosCrypt)
	for c in range(0,size):
		chave[dadosCrypt[c]]= dadosClear[c]
	arquivo = open('saida/chave.key','wb')
	count   = 0
	for c in chave:
		arquivo.write(str(c)+'\n')
		if c != 0 :
			count = count + 1

	arquivo = open("saida/t2SubstituicaoDescriptografado",'wb')
	for c in dadosCrypt:
		temp = chave[c]
		arquivo.write(chr(temp))

	arquivo.close()

	return chave



def caesar():
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

		

main()