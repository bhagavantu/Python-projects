# importing the csv module 
import csv 
  S
# field names 
fields = ['Name', 'Branch', 'USN', 'CGPA', 'Email id'] 
  
# data rows of csv file 
rows = [ ['Nikhil', 'ECE', '122', '8.0','abc@gmail.com'], 
         ['Sanchit', 'ECE', '22', '9.1','sanchith@gmail.com'], 
         ['Aditya', 'ISE', '24', '8.3','awe@gmail.com'], 
         ['Sagar', 'CSE', '111', '7.5','acfg@gmail.com'], 
         ['Prateek', 'ME', '13', '7.8','prateek@gmail.com'], 
         ['Akash', 'EI', '42', '6.1','akash@gmail.com']] 
  
# name of csv file 
filename = "placement_records.csv"
  
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
      
    # writing the fields 
    csvwriter.writerow(fields) 
      
    # writing the data rows 
    csvwriter.writerows(rows)