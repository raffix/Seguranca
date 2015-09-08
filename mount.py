import os

def main():
	stringArq	= './dicionario/speller/final'
	lista 		= os.listdir(stringArq)
	dicionario	= []

	for item in lista:
		arquivo = open(stringArq + '/' + item,'rb')
		linhas  = arquivo.readlines()
		for line in linhas:
			dicionario.append(line)
		arquivo.close()
	
	arquivo = open('saidaOff.txt','wb')
	linhas 	= arquivo.readlines()
	for line in linhas:
		dicionario.append(line)
	arquivo.close()

	dicionario.sort()
	saida  = open('saidaSpel.txt','wb')
	for line in dicionario:
		saida.write(line)
	saida.close()

main()