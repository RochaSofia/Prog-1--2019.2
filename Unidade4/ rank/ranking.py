'''
UFCG - PROG1
SOFIA ROCHA CAVALCANTI - 119210421
IMPRIME RANKING
'''
ultimoponto= 0
ultimaposicao=0

tamanho=int(input())

for i in range(tamanho):
	nome=(input())
	ponto=(int(input()))

	if ponto ==ultimoponto:
		posicao+= ultimaposicao
		print(posicao)
	else:
		posicao= i+1

	print('{}. {} ({})'.format(posicao,nome,ponto))
