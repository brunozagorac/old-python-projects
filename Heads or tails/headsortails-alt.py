from art import tprint
import random
import time

def coin_flipper():
    choice = input("Press F to flip the coin: ")

    if choice == "f" or choice == "F":
        print("Flipping...\n")
        time.sleep(1)
        print(flip)
        print("\nHopefully that solved your massive problem!\n")
    elif choice != "f" or choice != "F":
        coin_flipper()

coins = ("Heads", "Tails")
flip = random.choice(coins)

tprint("\n\nMade by Bruno\n")
print("Welcome to the coin-flipping program, your one-stop problem solver!\n")

coin_flipper()