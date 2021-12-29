
import random
name_string = input("enter the names of a person separated by commas ? ")
names = name_string.split(",")
length = len(names)
random_choice = random.randint(0, length-1)
print(random_choice)
