import random
print("Welcome to Hangman game!")

words=["Business","Portfolio","Adjustment"]

random_Selected_Word=random.choice(words)
To_fill_word=[]
for i in range(len(random_Selected_Word)):
    To_fill_word.append("_")

# print(random_Selected_Word)


print(f"Kindly start guessing for {To_fill_word}")
# UserInput=print("Enter a character to guess")