
print('''
** *****************************************************************************
          | | | |
 _________ | ________________.=""_; =.______________ | _____________________ | _______
| |, -"_,=""     `"=. | |
| ___________________ | __"=._o`"-._        `"=.______________ | ___________________
          | `"=._o`"=._      _`"=._ |
 _________ | _____________________ := ._o "=._."_. -= "'"=.__________________ | _______
| |    __.--" , ; `"=._o." ,-"""-._ ". |
|___________________ | _._"  ,. .` ` `` ,  `"-._"-._   ". '__ | ___________________
          |           |o`"=._` , "` `; .". ,  "-._"- ._; ;              |
 _________|___________ | ; `-.o`"=._; ." ` '`."\` . "-._ / _______________|_______
| | | o;    `"-.o`"=._``  '` ", __.--o; |
|___________________|_ |;     (  # ) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___ | o; ._    "      `".o | o_.--"; o; ____/______/______/____
/ ______/______/______/_"=._o--._; |;        ; ; / ______/______/______/_
____/______/______/______/__"=._o--._; o | o;     _._; o; ____/______/______/____
/ ______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/ ______/______/______/______/______/______/______/______/______/______ /
*******************************************************************************''')
print("welcome to the treasure island. \nyour mission is to find an treasure")
choice1 = input(' whether you want to take "Left" or "Right" ? ')

if choice1 == "left" or choice1 == "LEFT" or choice1 == "Left":
    choice2 = input('a person want to "swim" or "wait" ? ')
    if choice2 == "wait":
        choice3 = input(
            "you are arrived at the island unharmed. there is a three door , one red , one yellow , one blue, which colour do you choose ? ")
        if choice3 == "red":
            print("its a room full of fire. game over")
        elif choice3 == "yellow":
            print("heyy!! yippee you win this game ")
        elif choice3 == "blue":
            print("you enter the room of beast,game over ")
    else:
        print("you got attacked by an angry trout.game over")
else:
    print("you fell into the hole , your game is over")
