#################### VARIABLES & TYPES #####################
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

#################### LIST ########################
davidson_family = ["Adam", "Sarah", "Harper"]
print(davidson_family)
print(davidson_family[1])
new_fam = davidson_family + ["Preston"]
print(new_fam)

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
print(house[0][1])
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[:6]

# Use slicing to create upstairs
upstairs = areas[-4:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)