dadosCrypt = []
dicionario = []
acentos	   = [',','.','!','?','(',')','[',']','{','}',':',';','/','*','\/',"'",'-','+','%','$','@','_','=','^','~','|']

def readFile():
	entrada = input('Informe o arquivo criptografado: \t')
	arquivo = open(entrada,'rb')
	data    = arquivo.readlines()

	global dadosCrypt
	for line in data:
		for c in line:
			dadosCrypt.append(ord(chr(c)))	

	arquivo.close()


def carregaDicionarios():
	''' carrega os dicionarios ingles '''
	arquivo = open('dicionario.txt','rb')
	global dicionario
	linhas  = arquivo.readlines()
	arquivo.close()
	pos 	= chr(0)
	line	= []
	size 	= len(linhas)
	for c in range(0,size):
		if(pos == linhas[c][0]):
			line.append(linhas[c])
		else:
			pos = linhas[c][0]
			dicionario.append(line)
			line = []
			line.append(linhas[c])

	print ("Dicionario carregado")

def saidaCheck(dados):
	texto 	 = ''.join(dados)
	palavras = texto.split(' ')
	for palavra in palavras:
		
		for d in range(0,len(palavra)):
			flag = 0
			''' Procura por possivel  '''
			for e in acentos:
				if( e == palavra[d]):
					flag = 1
					break
			if( flag == 0 ):
				for pos in range(1,len(dicionario)):
					if(dicionario[pos][0][0] == ord(palavra[d])):
						found = 0
						for word in dicionario[pos]:
							if( str(word) in str(palavra) ):
								d =len(palavra)
								found = 1
								break
						if( d != len(palavra)):
							return -1
						if( found == 0 ):
							return -1
	return 1

def caesar():
	for chave in range(1,255):
		saida = []
		for c in dadosCrypt:
			saida.append(chr(((c + 256) - chave) % 256))
		''' Verifica se a saida e valida '''
		check = saidaCheck(saida)
		if( check != -1):
			return chave
	return -1

def transposicao():
	return -1

def vigenere():
	return ''

def substituicao():
	return ''

def main():
	carregaDicionarios()
	readFile()

	chave = caesar()
	if( chave != -1 ):
		print ("Caesar \t Chave: " + str(chave))
	chave = transposicao()
	if( chave != -1 ):
		print ("Transposicao \t Chave: " + str(chave))
	chave =  vigenere()
	if( len(chave) > 0):
		print ("Vigenere")
	chave = substituicao()
	if( len(chave) > 0):
		print ("Substituicao")

main()
	