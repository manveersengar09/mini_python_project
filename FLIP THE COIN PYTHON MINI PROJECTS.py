# FLIP THE COINS:

import random

def flip_coin():
    print("Welcome to the Coin Flip Simulator!")
    while True:
        flip = input("Flip the coin? (yes/no): ").lower()
        if flip == "yes":
            result = random.choice(["Heads","Tails"])
            print("🪙 You got:", result)
        elif flip == "no":
            print("Thanks for playing!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

# Call the function to start the simulator
flip_coin()
