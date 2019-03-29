str1= "abaracaca"
l1=list(str1)
dict1={}
for w in l1:
	if w in dict1.keys():
		dict1[w] = dict1[w] + 1
	else:
		dict1[w]=1
print(dict1)