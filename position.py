list1=[1,2,3,2,0,65,21,4,2,10]
search = int(input("enter serach element position"))
list2 =[]
for i,value in enumerate(list1):
	if value is search:
		list2.append(i)
print(list2)