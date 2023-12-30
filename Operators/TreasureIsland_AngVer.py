print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


#Write your code below this line 👇

print("Which road will you take ? Left or Right ")
path = input().lower()

if path == "left":
  print('You reached the port town. What will you do next ? Type "Swim" for swimming across or Type "Wait" to wait for a boat')
  path2 = input().lower()

  if path2 == "wait":

    gate = input("Great. You have reached the primodial gates. Choose the gate : Red, Blue or Yellow.\n").lower()
    #we just used a variable to hold the INPUT received and avoided the Print statement line.

    if gate == "yellow":
      print("You Win!")

    elif gate == "red":
      print("You Die! Burnt by primodial fire.")

    elif gate == "blue":
      print("You die! Eaten by beasts")

    else:
      print("Game Over")

  else:
    print("Game Over. You got eaten by a shark.")

else:
  print(" Game Over. You got attacked by a Dragon.")

  
