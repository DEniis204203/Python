cat = ["c","a","t"]
for letter in cat:
	print(letter)
print("-------------------------------------------")
animals = ["fish","mushroom","fruit"]
for index in range(len(animals)):
	print(index,animals[index])
print("--------------------EX 1------------------------")
spisok = [2,7,8,11,12,3,1,0,4,-2,5,21]
result = 0
result1 = 1
for item in spisok:
	if item > 10:
		result = result + item
		continue
	if item > 0 < 10:
		result1 = result1*item
		continue
	if item <= 0:
		continue
print(result)
print(result1)	
print("--------------------Ot cheloveka------------------------")
strv = input()
print(strv)




