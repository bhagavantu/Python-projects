year = int(input("enter the year"))
if((year%4==0 and year%100!=0) or (year%400==0)):
 	print('leap')
else:
 	print('not leap')
     