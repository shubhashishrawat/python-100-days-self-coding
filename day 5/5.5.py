import random
letter = ['A', 'B', 'C', ' D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['@', '#', '$', '%', '&', '*', '(', ')', '+', '_']
nm_letter = int(input("how many letter you want to enter : "))
nm_number = int(input("how many  number you wanna enter : "))
nm_symbol = int(input("how much symbol you wanna enter : "))
password_list = []
for char in range(1, nm_letter + 1):
    password_list.append(random.choice(letter))
for char in range(1, nm_number + 1):
    password_list.append(random.choice(number))
for char in range(1, nm_symbol + 1):
    password_list.append(random.choice(symbol))
    print(password_list)
random.shuffle(password_list)
print(password_list)
password = " "
for char in password_list:
    password += char
print(f" your password is : {password}")
