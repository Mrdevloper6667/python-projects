letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random

password_list = []

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
for random_char  in range(0,nr_letters):
    password_list.append(random.choice(letters))
nr_symbols = int(input(f"How many symbols would you like?\n"))
for random_symbol  in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
nr_numbers = int(input(f"How many numbers would you like?\n"))
for random_number  in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)

random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(password)