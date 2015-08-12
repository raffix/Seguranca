dados = []

def readFile():
	entrada = raw_input('Informe o arquivo de entrada:\t ')
	arquivo = open(entrada,'rb')
	global dados
	data = arquivo.readlines()
	for line in data:
		for c in line:
			dados.append(c)

	arquivo.close()
	

def ceasar(chave):
	readFile()
	saida = raw_input("Informe o arquivo de saida:\t ")
	arquivo = open(saida,'wb')
	''' map(charPlus,dados) '''
	for c in dados:
		caracter = ord(c) + chave
		caracter = caracter % 256
		arquivo.write(chr(caracter))

	arquivo.close()

	print "\n\tConcluido Caesar\n"

	''' descriptografa '''

	arquivo = open(saida,'rb')
	saida2 = 'DESCRIPTOGRAFADO'+saida
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
	saida = raw_input("Informe o arquivo de saida:\t ")
	arquivo = open(saida,'wb')
	lista = []
	for line in dados:
		for c in line:
			lista.append(c)

	restChar = len(lista) % chave
	if( restChar != 0 ):
		c = 0
		''' Adiciona os caracteres para fechar a matriz '''
		while c < restChar:
			lista.append('')
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

	''' Transposicao da matriz e gravacao '''
	for d in range(0,chave):
		for c in range(0,restChar):
			arquivo.write(matriz[c][d])


def vigenere(chave):
	readFile()
	saida   = raw_input("Informe o arquivo de saida:\t ")
	arquivo = open(saida+".encrypted",'wb')
	resto   = len(dados) % len(chave)

	''' Soma os caracteres '''
	c = 0

	while c < len(dados):
		for i in range(0,len(chave)):
			if ( c == len(dados)):
				break
			temp = ord(dados[c]) + ord(chave[i])
			arquivo.write(str(temp))
			c = c + 1

	arquivo.close()

	print "\n \t Vigenere Concluido"


def substituicao():
	readFile()
	saida   = raw_input("Informe o arquivo de saida:\t ")
	arquivo = open(saida+".encrypted",'wb')

	



def main():
	metodo = int(raw_input("\n Escolha o metodo de criptografia: \n\t1 - Cifra de Caesar \n\t2 - Cifra de transposicao \n\t3 - Cifra de vigenere\n\t4 - Cifra de substituicao\nEntrada: "))
	
	if metodo == 1 :
		chave = int(raw_input("\n\n\t Cifra de CAESAR \nInforme o valor da chave:\t "))
		ceasar(chave)

	elif metodo == 2 :
		chave = int(raw_input("\n\n\n Cifra de TRANSPOSICAO \n\n\nInforme o valor da chave: "))
		transposicao(chave)

	elif metodo == 3 :
		chave = raw_input("\n\n\n Cifra de VIGENERE \n\n\nInforme o valor da chave: ")
		vigenere(chave)
	elif metodo == 4 :
		chave = 256
		print "\n\n\n Cifra de SUBSTITUICAO \n\n"
		substituicao()


	else :
		print "\n\n\nNenhuma cifra valida escolhida \n "
		return
		

main()
