age = input("enter your age")
age_as_int = int(age)
years_remaining = 90 - age_as_int
months_remaining = years_remaining*12
days_remaining = years_remaining*365
weeks_remaining = years_remaining*52
print(
    f"you have months {months_remaining}, days {days_remaining} ,weeks{weeks_remaining}")
