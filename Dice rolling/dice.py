from art import tprint
import random


roll = "y"

print(" ")
print(" ")
tprint("Made by Bruno")
print(" ")
print("This is a dice-rolling simulator for those who prefer virtual dice")
print(" ")
print("Press Y to roll the dice")
print(" ")
while roll == "y":

    # Generate a random number
    # between 1 and 6
    number = random.randint(1,6)

    # prints an ASCII of a dice

    if number == 1:
        print("[-----]") 
        print("[     ]") 
        print("[  0  ]") 
        print("[     ]") 
        print("[-----]")
    if number == 2: 
        print("[-----]") 
        print("[ 0   ]") 
        print("[     ]") 
        print("[   0 ]") 
        print("[-----]") 
    if number == 3: 
        print("[-----]") 
        print("[     ]") 
        print("[0 0 0]") 
        print("[     ]") 
        print("[-----]") 
    if number == 4: 
        print("[-----]") 
        print("[0   0]") 
        print("[     ]") 
        print("[0   0]") 
        print("[-----]") 
    if number == 5: 
        print("[-----]") 
        print("[0   0]") 
        print("[  0  ]") 
        print("[0   0]") 
        print("[-----]") 
    if number == 6: 
        print("[-----]") 
        print("[0 0 0]") 
        print("[     ]") 
        print("[0 0 0]") 
        print("[-----]") 

    roll=input("Press Y to roll again and any other key to quit: ")
    if not roll.isalpha():
        print ("Wrong key! Try again.")
