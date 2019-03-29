from capstone_boilerplate import PlacementManagement

stud1 = PlacementManagement('bhagavantu', 123, 8, "a@a.com", 'ece',345,786)
print(stud1.cgpa)
stud1.eligibility()

stud1.applied()

stud_dict=stud1.details()


stud_dict