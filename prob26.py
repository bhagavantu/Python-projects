mylist = []
def add_to_list(word):
	mylist.append(word)
for i in range(4):
	word = input("enter the names:")
	add_to_list(word)

print(mylist)