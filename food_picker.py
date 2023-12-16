import random
file = open("food_list")

print(random.choice(file.read().split()))

file.close()
