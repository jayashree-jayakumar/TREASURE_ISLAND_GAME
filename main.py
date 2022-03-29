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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
Direction=input('You\'re at a Cross Road.\nWhere want to go? "left" or "right"\n').lower()
if (Direction=="left"):
    Island=input('You reached a Lake which surrounds the Island.What do you want to \'wait for a boat\' or \'swim\'?.\nThen choose "swim" or "wait".\n').lower()
    if (Island=="wait"):
        Door_choosing=input('You reached the Island. Now you are standing in front of three types of colour door.\nWhat colour door do you want to choose ? "Red" or "Blue" or "Yellow"\n').lower()
        if (Door_choosing=="red"):
            print("...GAME OVER...\nYou have caught up with Wolves.")
        elif (Door_choosing=="blue"):
            print("...GAME OVER...\nYou have died by Bomb Blast.")
        else:
            print("...WIN...\nYou have entered the Treasure Room.")
    else:
        print("...GAME OVER...\nYou have killed by the lurking Goonch Catfish.")
else:
    print("...GAME OVER...\nYou have fallen into the Pit.")
