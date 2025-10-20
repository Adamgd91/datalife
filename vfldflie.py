########## VARIABLES & F-STRING ###########

va1 = "Adam"
va2 = "Davidson"
age = 34
profession = "AI/ML Engineer"
is_meet = False
family_names = ["Adam", "Sarah", "Harper"]
ages = [34, 32, 1]

full_name = f'{va1} {va2}'
print(full_name)

########## DICTS & LISTS ###########

scores = [55, 66, 76, 99, 87, 76, 68, 98, 88, 87, 80, 78, 75, 69, 100]
passed_scores = []
failed_scores = []

for i in scores:
    if i >= 70:
        passed_scores.append(i)
    else:
        failed_scores.append(i)
        
count_passed = len(passed_scores)
count_failed = len(failed_scores)   
print(f'There are {count_passed} scores that passed : {passed_scores}')
print(f'There are {count_failed} scores that passed : {failed_scores}')

family = {
    "Adam" : 34,
    "Sarah" : 32,
    "Harper" : 3,
    "Preston" : 5
}

for name, age in family.items():
    if age == 34:
        print(f'Adam is {name} years old')