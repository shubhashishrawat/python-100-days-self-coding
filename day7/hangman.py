import random
word_list = ["ardvark", "padharu", "elephant", "camel", "baboon"]
chosen_word = random.choice(word_list)
guess = input("enter any letter from the word :").lower()
for letter in chosen_word:
    if guess == letter:
        print("right")
    else:
        print("wrong")
