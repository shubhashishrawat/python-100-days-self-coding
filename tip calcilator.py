print("welcome to the tip calculator")
bill_input = input("what was the total bill ?")
tip_input = input("what percentage tip would you like to give ? 10,20,30 ")
people = input("how many people to split the bill ?")
half_bill = int(bill_input)*(int(tip_input)/100)
full_bill = (int(bill_input) + int(half_bill))
total_bill = (int(full_bill)/int(people)
print(f" each person should pay : rs{total_bill}")
