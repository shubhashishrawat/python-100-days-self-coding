height = float(input("enter your height in m:"))
weight = float(input("enter your weight in kg:"))
bmi = (weight)/(height**2)
if bmi < 18.5:
    print(f"your bmi is {bmi}, they are underweight")
elif bmi >= 18.5:
    print(f"your bmi is {bmi}, they are normal weight")
elif bmi <= 25:
    print(f"your bmi is {bmi}, they are overweight")
elif bmi < 30:
    print(f"your bmi is {bmi}, they are obese")
else:
    print(f"your bmi is {bmi}, 1they are clinically obese")
