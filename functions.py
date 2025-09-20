kids = "Harper"

print(len(kids))

def testing():
    print("Hello")
    
testing()

######## BUILT IN FUNCTIONS ##########
ages = [11, 32, 54, 65, 22, 31 ,76, 66, 54,]
can_drink = []
too_young = []
oldest = max(ages)
print(oldest)

def drinking_age():
    for i in ages:
        if i >= 21:
            can_drink.append(i)
        else:
            too_young.append(i)
drinking_age()
num_drinking = len(can_drink)
num_not_drinking = len(too_young)
print(can_drink)
print(num_drinking)

print(too_young)
print(num_not_drinking)