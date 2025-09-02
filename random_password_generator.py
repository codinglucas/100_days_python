# Random Password Generator

# This script creates a password of x-letters, y-symbols and z-numbers at random positions


import random
password = [None]

n_letters = int(input("number of letters: "))
n_symbols = int(input("number of symbols: "))
n_numbers = int(input("number of numbers: "))

letters = "abcdefghijklmnopqrstuwxyz"
letters = list(letters)

symbols = "!@#$%¨&*"
symbols = list(symbols)

numbers = "0123456789"
numbers = list(numbers)

n_char = n_letters + n_symbols + n_numbers
password = [None] * n_char
print(len(password))


for x in range(0, n_letters):
    random_letter = random.choice(letters)
    random_index = random.randint(0, len(password)-1)
    while password[random_index] != None:
        random_index = random.randint(0, len(password)-1)
    password[random_index] = random_letter

for x in range(0, n_symbols):
    random_letter = random.choice(symbols)
    random_index = random.randint(0, len(password)-1)
    while password[random_index] != None:
        random_index = random.randint(0, len(password)-1)
    password[random_index] = random_letter

for x in range(0, n_numbers):
    random_letter = random.choice(numbers)
    random_index = random.randint(0, len(password)-1)
    while password[random_index] != None:
        random_index = random.randint(0, len(password)-1)
    password[random_index] = random_letter

# can also use random.shuffle from random lib, as it goes: password = ['char1', 'char2'...] -> random.shuffle(password)
print(''.join(password))
