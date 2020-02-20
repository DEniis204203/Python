list=[2,5,7,14,28,-25,47]
result=0
index=0
while True:
	while index < 7:
		list[index]+=1
		index += 1
	while index<7:
		result=result+list(index)
		index += 1
	if result>7487:
		print(list)
		print(result)
		break
	else:
		result = 0
		
	 

