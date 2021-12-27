leap_year = int(input("enter the year"))
if leap_year % 4 == 0:
    if leap_year % 100 == 0:
        if leap_year % 400 == 0:
            print("its a leap year:")
        else:
            print("its not a leap year:")
    else:
        print("its a leap year:")
else:
    print("its not a leap year:")
