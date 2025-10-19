import numpy as np

height = [1.73, 1.68, 1.89, 1.79, 1.53, 1.68]
weight =  [65.4, 59.2, 88.4, 68.7, 94.3, 79.9]
np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height ** 2
print(bmi)

high_bmi = bmi[bmi > 23]
count_bmi = len(high_bmi)
print(f'There are {count_bmi} number of high BMIs: {high_bmi}')