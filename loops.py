areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
for i in areas:
    if i == "bedroom":
        print(areas[5])
        
        

scores = [12,9,8,34,22,1,14,12]
failed = []
for i in scores:
    if i < 12:
        failed.append(i)

num_failed = len(failed)
print(num_failed)

counting_scores = scores.count(12)
print(f'The number 12 is in this list {counting_scores} times!')
print(scores.index(34))