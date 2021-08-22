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
print("You've arrived here by canoe and have found yourself on the island with some very dense foliage.")
print("You can either go right and walk along the beach to find an easy way in or try and hack your way through")
gameover = ('''
  __ _  __ _ _ __ ___   ___      ___ __     __ ___  _ __
 / _` |/ _` | '_ ` _ \ / _ \   / _  \  \   / // _ \|  __|
| (_| | (_| | | | | | |  __/  | (_|  |\ \_/ /|  __/|  |
 \__, |\__,_|_| |_| |_|\___|   \____/  \___/  \____|__|
  __/ |
 |___/
 ''')

step_1 = input("Do you go right or into the bush? Type 'go right' or 'go into the bush'\n").lower()
if step_1 == "go right":
    print("You see a large mysterious looking tree stump next to what used to be a frequented path.")
    step_2 = input("Do you walk down the path or investigate the mysterious tree stump. Type 'investigate' or 'walk down path'\n").lower()
    if step_2 == "investigate":
        print("You find a box with a note that shows a path to a bridge with warning that mentions that the piles of bush are covering trap holes")
        step_3 = input("You walk down the path and avoid the piles of brush. At the end of the path is a bridge that is falling apart.\n Do you try the bridge or do you find a way down to the river? Type 'try bridge' or 'find a way down'\n").lower()
        if step_3 == "find a way down":
            print("You make your way down to the river. It's moving fast")
            step_4 = input("Do you try and cross the river or go back to the bridge? Type 'cross river' or 'go back to the bridge'\n").lower()
            if step_4 == "cross river":
                print("The current picks you up but you're able to get across about 100m downstream. You notice there is a cave ahead.\n As you walk closer and shine your light, you see 3 doors.\n The first door looks old and made of stone.\n The second door has a backpack laying againts it.\n The third door is slightly open.")
                step_5 = input("Do you open door 1, check out the backpack, or open the slightly open door?\nType 'open door 1', 'check backpack', or 'open slightly open door'\n").lower()
                if step_5 == "open door 1":
                    print("The door is jammed.")
                    step_6 = input("Do you try and backpack or the slightly open door?\n Type 'check backpack' or 'slightly open door'\n").lower()
                    if step_6 == "check backpack":
                        print(f"Oh no! A Black Mamba bit you.\n {snake}")
                        print(gameover)
                    else:
                        print("You start to hear a very mysterious hum. You walk down the dark tunnel with you flashlight and as you get to the end, the hum gets louder.")
                        print("You turn the corner and see piles upon piles of treasure!")
                elif decision5 == "check backpack":
                    print(f"Oh no! A Black Mamba bit you.\n {snake}")
                    print(gameover)
                else:
                    print("You start to hear a very mysterious hum. You walk down the dark tunnel with you flashlight and as you get to the end the hum gets louder.")
                    print("You turn the corner and see piles upon piles of treasure! You won!")
            else:
                print(f"You went back to the bridge and tried to cross it. Oh no! it starts to fall apart and you fall 50ft into the river. \n {gameover}")
        else:
            print(f"Oh no! the bridge is falling apart and you fall 50ft into the river. \n {gameover}")
    else:
        print(f"Oh no! You stepped onto a pile of brush that was covering a hole. \n {gameover}")
else:
    print(f"Oh no! As you were hacking your way into the bush, a puma jumped you.\n")
    print(gameover)
