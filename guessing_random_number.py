import random

print("Welcome to Guessing Number Game")

dif_choice = input("Hard or easy mode? ").lower().strip("")

if dif_choice == "hard":
    life = 5
else:
    life = 10

random_number = random.randint(1, 100)

def compare(g_number, actual_number=random_number):
    if g_number > actual_number:
        return "Too high"
    elif g_number < actual_number:
        return "Too low"

print(f"Hint: {random_number}")

while life != 0:
    print(f"You have {life} lifes remaining!")
    guess_number = int(input("Guess a number: "))

    if guess_number != random_number:
        print(compare(guess_number))
    else:
        print(f"You won! The secret number was {random_number}")
        break

    life -= 1
    if life == 0:
        break
    else:
        print("Guess again!")
        print("----------------------")
