from art import tprint
import random
import time

coins = ("Heads", "Tails")
flip = random.choice(coins)

print(" ")
print(" ")
tprint("Made by Bruno")
print(" ")
print("Welcome to the coin-flipping program, your one-stop problem solver!")
print(" ")
choice = input("Press F to flip the coin: ")

if choice == "f" or choice == "F":
    print("Flipping...")
    print(" ")
    time.sleep(1)
    print(flip)
    print(" ")
    print("Hopefully that solved your massive problem! ")
    print(" ")
else:
    print(" ")
    print(" ")
    print("Program quit.")
    print(" ")
    quit()