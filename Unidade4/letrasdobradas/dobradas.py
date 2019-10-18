dobradas=[]
n_dobradas=[]

tamanho=int(input())

for i in range(tamanho):
	entrada= False
	palavra=input()
	

	for elemento in range(len(palavra)-1):
		if palavra[elemento]== palavra[elemento+1]:
			entrada=True
			break

	if entrada==True:
		dobradas.append(palavra)
	else:
		n_dobradas.append(palavra)

print('{} palavra(s) com letras dobradas:'.format(len(dobradas)))
for i in range(len(dobradas)):
	print(dobradas[i])
print('---')
print('{} palavra(s) sem letras dobradas:'.format(len(n_dobradas)))
for i in range(len(n_dobradas)):
	print(n_dobradas[i])




