from capstone_boilerplate import PlacementManagement

stud1 = PlacementManagement('bhagavantu', 123, 9, "a@a.com", 'ece')
print(stud1.cgpa)
stud1.eligibility()
stud1.applied()