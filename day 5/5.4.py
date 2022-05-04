for value in range(1, 101):
    if value % 3 == 0 and value % 5 == 0:
        print("fizzbuzz")
    elif value % 5 == 0:
        print("buzz")
    elif value % 3 == 0:
        print("fizz")
    else:
        print(value)
