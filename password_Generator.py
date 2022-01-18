#
# Author- Jisha Maniamma
#
import random;

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

Number_Character = int(input("How many letters would you like in your password?\n"))
Number_Numbers = int(input("How many symbols would you like?\n"))
Number_speacialCharacters = int(input("How many numbers would you like?\n"))

password = []
for letter in range(0, Number_Character):
    password.append(random.choice(letters))

for numbr in range(0, Number_Numbers):
    password.append(random.choice(numbers))

for symbo in range(0, Number_speacialCharacters):
    password.append(random.choice(symbols))

random.shuffle(password)

password_ = ""
for char in password:
    password_ += char


print(f"The password generator generate password is- {password_}")
