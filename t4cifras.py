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



def main():
	readFile()

	
	

main()