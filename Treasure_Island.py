print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"').lower()
if choice1 == "right":
  print("You fell into a hole. Game Over.")
if choice1=="left":
  print("You have come to a lake. There is an island in the middle of the lake.")
  choice2 = input('Type "wait" to wait for a boat. Type "swim" to swim')
  if choice2 == "swim":
    print("There is a snake in the water. Game Over.")
  else:
    print("You arrive at the island unharmed. There is a house with 3 doors. One red,One blue, One yellow.")
    choice3 = input('Which color do you choose?')
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    if choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    if choice3 == "yellow":
      print("You found the treasure! You Win!")
