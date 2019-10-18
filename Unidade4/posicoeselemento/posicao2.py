

num=input()
sequencia=input().split()
igual=False


x=''


for i in range(len(sequencia)):
	if sequencia[i]== num :
		x+= str(i) + " "
		igual= True

x=x[:len(x)-1]
if igual== True:
	print(x)
	
else:
	print('-1')




