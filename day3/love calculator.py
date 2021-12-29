print("Welcome to the love calculator")
first_per_name = input("what is your name ?\n")
second_per_name = input("what is her name ?\n")
combined_string = first_per_name + second_per_name
lower_case_string = combined_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l + o + v + e
love_score = str(true) + str(love)
print(f"your score is :{love_score}")
