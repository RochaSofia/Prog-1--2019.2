num=[]
soma=0

for i in range(11):
	num.append(input())

for i in range(1,len(num)):
	if int(num[i])%int(num[0]) == 0  :
		soma+= int(num[i])

print(soma)
