dict1 = {'a':"speckbit", 'b':"world", 'c':"quiet"}
def getKeysByValue(a, b):
    Keys = list()
    Items = a.items()
    for item  in Items:
        if item[1] == b:
            Keys.append(item[0])
    return  Keys

Keys = getKeysByValue(dict1, "speckbit")
ft= 'key'



for c  in Keys:
	print(f'{ft} is',c)
	