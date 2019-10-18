entrada = input()
sequencia= input().split()

igual= False


for i in range(len(sequencia)):
	if entrada == sequencia[i] :
		igual= True
		break

if igual == True :
	print('sim')
else:
	print('não')
