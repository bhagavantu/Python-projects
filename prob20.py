usn= [1,2,3]
names = ["ramesh","suresh", "andy"]
database={}
for key in usn: 
    for value in names: 
        database[key] = value 
        names.remove(value) 
        break
print(database)