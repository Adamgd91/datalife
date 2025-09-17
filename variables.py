fname = "Adam"
lname = "Davidson"
full_name = f'My name is {fname} {lname}'
age = 34
career = "AI/ML Engineer"
accomplished = False
height = 1.79
weight = 68.7
bmi = weight / height ** 2

print(full_name)
print(f'I am {age} and I will become an {career}!')
print(bmi)
print(type(accomplished))
print(type(bmi))

#################### LIST #####################
davidson_family = ["Adam", "Sarah", "Harper"]
print(davidson_family)

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
        ["bedroom", bed],
        ["bathroom", bath]]

# Print out house
print(house)