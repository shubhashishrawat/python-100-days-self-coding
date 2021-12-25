height = input("enter your height in m")
weight = input("enter your weight in kg")
bmi = int(weight)/float(height)**2
print("bmi of the person is", bmi)
if bmi > 25:
    print("person is obese")
