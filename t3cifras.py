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

	dicionario[0] = "RaffaelCicilianoRossi"
	dicionario.remove("RaffaelCicilianoRossi")
	print ("Dicionario carregado")

def searchWord(group, palavra):
    for word in group:
    	if(word in palavra):
    		return 1
    return 0
    
def searchPositionDictionary(firstLetter):
	for index in range(0,len(dicionario)):
		if(dicionario[index][0][0] == firstLetter):
			return index
	return -1

def saidaCheck(dados):
	text = dados.split(' ')
	for word in text:
		print(word)
		firstLetter = word[0]
		letterPosition = searchPositionDictionary(firstLetter)
		if( letterPosition == -1):
			return -1

		trueWord = 0
		for position in range(0,len(dicionario[letterPosition])):
			if(word == dicionario[letterPosition][position]):
				trueWord = 1
				position = len(dicionario[letterPosition])
		if( trueWord ==  0):
			''' maybe this word is a accent '''
			for item in acentos:
				if( item in word):
					trueWord = 1
		if( trueWord == 0):
			return -1

	return 1

def checkToken(token):
    for c in acentos:
        if( token == c ):
            return 1
    return 0


def caesar():
	for chave in range(62,63):
		saida = []
		for c in dadosCrypt:
			saida.append(chr(((c + 256) - chave) % 256))
		''' Verifica se a saida e valida '''
		text = ''.join(saida)
		check = saidaCheck(text)
		if( check != -1):
			return chave
	return -1

def transposicao():
	return -1

def vigenere():
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
