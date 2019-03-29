day= int(input("enter the day:"))
month= int(input("enter the month:"))
year = int(input("enter the year"))
if (day<32) and (month<13):
	print("valid day:")
else:
	print("not valid")


	
if((year%4==0 and year%100!=0) or (year%400==0)):
 	print('leap')
else:
 	print('not leap')
     