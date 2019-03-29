companies = {'google':7,'microsoft':8,'tesla':8.5,'facebook':8.2}
students_data = {}

class PlacementManagement:
	"""
	General Data Class for a place Management
	"""

	def __init__(self, name, usn,cgpa, email, branch, id_number, password):
		"""
		Constructor function for the Data Class
		Executed by interpreter to create an instance of this class.
		Attributes:
			self.name -- name of the student (str)
			self.usn -- usn of student  
			self.cgpa -- cgpa of the student (float)
			self.email --  email id of student
			self.branch -- branch of student (str)
			self.id_no -- id number to create the placement data (int)
			self.password -- password to access the account
		"""
		self.name = name
		self.usn = usn
		self.cgpa = float(cgpa)
		self.email = email
		self.branch = branch
		self.id_number = id_number
		self.password= password 	

	def eligibility(self):
		# To check the elibility of student for the placement

		if self.cgpa > 6.5:
			print("Eligible for the placement")
				
		else:
			print("Sorry! not eligible for placement")

	def applied(self):
		# To find the various of companies applied by the student
		print(companies)  # it gives the list of companies
		
		for company, comp_cgpa in companies.items():
			#It compares the student cgpa with company cgpa
			if self.cgpa >= comp_cgpa:
				print(self.name)
				print("applied company name is:",company)
				
				
		else:
				print("You not applied for this company:", company)


	def details(self):
		# To get the  student full details
		print("candidate details:")

		print("name:", self.name)
		print("usn:", self.usn)
		print("email:", self.email)
		print("cgpa:", self.cgpa)
		print("branch:", self.branch)


	#-------------------------------------
	#child class1
class candidate(PlacementManagement):

	def __init__(self, name, usn,cgpa,email, branch):
		self.name = name
		self.usn = usn
		self.email = email
		self.branch = branch
		self.cgpa =comp_cgpa


		if cgpa < 6.5:
			print("minimum cgpa will be 6.5 ")
		else:
			self.cgpa = cgpa

# child class2
class p_candidate(PlacementManagement):

	def __init__(self, name, usn, email,cgpa, branch):
		self.name = name
		self.usn = usn
		self.email = email
		self.branch = branch
		










