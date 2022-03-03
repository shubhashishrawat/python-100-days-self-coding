#import random
#name_string = input("enter the names of a person separated by commas ? ")
#length = len(names)
#random_choice = random.randint(0, length-1)
#person_who_will_pay_bill = names[random_choice]
#print(person_who_will_pay_bill + " is buy a meal for evryone")
import random
name_string=input("enter your name by commas ? ")
name = name_string.split(" , ")
person_who_will_pay_bill =random.choice (name)
print(person_who_will_pay_bill + " give you a treat ")