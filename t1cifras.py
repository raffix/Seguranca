dados = []

def readFile():
	entrada = input('Informe o arquivo de entrada:\t ')
	arquivo = open(entrada,'rb')
	global dados
	data = arquivo.readlines()
	for line in data:
		for c in line:
			dados.append(c)

	arquivo.close()
	

def ceasar(chave):
	readFile()
	saida = input("Informe o arquivo de saida:\t ")
	arquivo = open(saida,'wb')
	''' map(ord,dados) '''
	for c in dados:
		caracter = ord(c) + chave
		caracter = caracter % 256
		arquivo.write(chr(caracter))

	arquivo.close()

	print ("\n\tConcluido Caesar\n" )

	''' descriptografa '''

	arquivo = open(saida,'rb')
	saida2 = saida + 'DESCRIPTOGRAFADO'
	arquivo2 = open(saida2,'wb')
	dadosCrip = arquivo.readlines()
	for line in dadosCrip:
		for c in line:
			caracter = int(ord(c)) - chave
			caracter = caracter % 256
			arquivo2.write(chr(caracter))

	arquivo.close()
	arquivo2.close()


def transposicao(chave):
	readFile()
	matriz = []
	saida = input("Informe o arquivo de saida:\t ")
	arquivo = open(saida,'wb')
	lista = []
	for line in dados:
		for c in line:
			lista.append(c)

	restChar = len(lista) % chave
	if( restChar != 0 ):
		restChar = chave - restChar
		c = 0
		''' Adiciona os caracteres para fechar a matriz '''
		while c < restChar:
			lista.append(chr(0))
			c = c +1

	restChar = len(lista) / chave
	matriz = []
	pos = 0

	''' Gera a matriz '''
	for c in range(0,restChar):
		linha = []
		for d in range(0,chave):
			linha.append(lista[pos])
			pos = pos + 1
		matriz.append(linha)

	lista = []

	''' Transposicao da matriz e gravacao '''
	for d in range(0,chave):
		for c in range(0,restChar):
			lista.append(matriz[c][d])

	for c in lista:
		arquivo.write(c)


	arquivo.close()

	print ("\n\n Transposicao Concluido" )
	return


def vigenere(chave):
	readFile()
	saida   = input("Informe o arquivo de saida:\t ")
	arquivo = open(saida+".enc",'wb')
	resto   = len(dados) % len(chave)

	''' Soma os caracteres '''
	c = 0

	while c < len(dados):
		for i in range(0,len(chave)):
			if ( c == len(dados)):
				break
			temp = (ord(dados[c]) + ord(chave[i])) % 256
			arquivo.write(chr(temp))
			c = c + 1

	arquivo.close()




	''' descriptografa '''

	arquivo   = open(saida+".enc",'rb')
	saida2    = saida + 'DESCRIPTOGRAFADO'
	arquivo2  = open(saida2,'wb')
	listaCrip = []
	dadosCrip = arquivo.readlines()
	for line in dadosCrip:
		for c in line:
			listaCrip.append(c)
	c = 0 

	while c < len(dados):
		for i in range(0,len(chave)):
			if ( c == len(dados)):
				break
			temp = ((ord(listaCrip[c]) - ord(chave[i])) + 256 ) % 256
			arquivo2.write(chr(temp))
			c = c + 1

	arquivo.close()
	arquivo2.close()


	print ("\n \t Vigenere Concluido" )
	return


def criptografaSubstituicao(chave):
	readFile()
	saida        = input("Informe o arquivo de saida:\t ")
	arquivo      = open(saida+".enc",'wb')
	arquivoChave = open(chave,'r')
	tempTranspos = arquivoChave.readlines()
	chave 		 = []

	for line in tempTranspos:
			chave.append(int(line))

	for c in dados:
		item = int(chave[ord(c)])
		arquivo.write(chr(item))
	arquivo.close()

	arquivo   = open(saida+".enc",'rb')
	saida2    = saida + 'DESCRIPTOGRAFADO'
	arquivo2  = open(saida2,'wb')
	dadosCrip = arquivo.readlines()

	for line in dadosCrip:
		for c in line:
			valor = buscaCharPos(ord(c),chave)
			arquivo2.write(chr(valor))

	arquivo2.close()

	print ("\n SUBSTITUICAO Concluido" )
	return



def buscaCharPos(token, lista):
	d = 0
	for c in lista:
		if( c == token ):
			return d
		d = d + 1
	return -1

def main():
	metodo = int(input("\n Escolha o metodo de criptografia: \n\t1 - Cifra de Caesar \n\t2 - Cifra de transposicao \n\t3 - Cifra de vigenere\n\t4 - Cifra de substituicao\nEntrada: "))
	
	if metodo == 1 :
		chave = int(input("\n\n\t Cifra de CAESAR \nInforme o valor da chave:\t "))
		ceasar(chave)

	elif metodo == 2 :
		chave = int(input("\n\n\n Cifra de TRANSPOSICAO \n\n\nInforme o valor da chave: "))
		transposicao(chave)

	elif metodo == 3 :
		chave = input("\n\n\n Cifra de VIGENERE \n\n\nInforme o valor da chave: ")
		vigenere(chave)
	elif metodo == 4 :
		
		chave = input("\n\n\n Cifra de SUBSTITUICAO \n\n\nInforme o arquivo da chave: \t")
		criptografaSubstituicao(chave)


	else :
		print ("\n\n\nNenhuma cifra valida escolhida \n " )
		return
		

main()
