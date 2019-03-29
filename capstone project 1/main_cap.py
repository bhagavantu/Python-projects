
from placement import PlacementManagement
""" 
**Variables** 
Student_data: (dict) {id_number: placement management Object} holds all the accounts created during the session. 
id_no: (int) - Set to 0 by default ,id number . allocation starts here. Incremented after every new placement data
creation 
"""

students_data={}
id_number = 0
print(" Welcome to placement management")
# Application Loop

while True:
	print("Hey! What would you like to do today?\n\n\
		1. Create Placement Data\n\
		2. Check Eligibility\n\
		3. show applied details\n\
		4. candidate full details\n\
		5. Exit\n")
	# Print the options in a table
	"""print(tabulate([(1, " Create Placement Data ",), (2, " Check Eligibility ",), (3, " applied details ",), (4, " full details ",)], tablefmt="fancy_grid"))"""

	choice = int(input("Enter your option: "))

	if choice == 1:
		"""If user choice is 1 (int) – Create new placement data with info """

		# Ask for basic info needed to create a data
		name = input("Enter your name: ")
		usn = input("Enter your usn: ")
		cgpa = input("Enter your cgpa: ")
		email =input("Enter your email: ")
		branch = input("Enter your department: ")
		password =input("Enter your password: ")

		# Use the current id_number count to assign an id number and save the object as students_data
		students_data[id_number]=PlacementManagement(name, usn,cgpa, email, branch, id_number, password)
		print(students_data)


		print(f"Placement Data created successfully! Your  Placement ID number is {id_number}")
		# Increment the count after successful creation of placement data
		id_number =id_number + 1
	

	elif choice ==2:
		""" 
		If user choice is 2 (int) - perform eligibility process 
		"""
		# Get User Account Details
		id_no =eval(input("Enter the ID number: "))
		upassword = input("Enter the password: ")

		# To check the elibility of student for the placement
		if upassword == students_data[id_no].password:
			students_data[id_no].eligibility()
		else:
			print("\n\nInvalid Details. Please enter again!\n\n")

	elif choice ==3:
		""" 
		If user choice is 3 (int) – perform process of  student applied for the placement
		"""
		# Get User Account Details
		id_no =eval(input("Enter the ID number: "))
		upassword = input("Enter the password: ")

		# To find the various of companies applied by the student
		if upassword == students_data[id_no].password:
			students_data[id_no].applied()

		else:
			print("\n\nInvalid Details. Please enter again!\n\n")


	elif  choice ==4:
		""" 
		If user choice is 4 (int) – show full details of student
		"""

		# Get User Account Details
		id_no = eval(input("Enter the ID number: "))
		upassword = input("Enter the password: ")

		# To get the  student full details
		if upassword == students_data[id_no].password:
			students_data[id_no].details()
		else:
			break
	# Exit the loop if input is invalid.

	else: break




