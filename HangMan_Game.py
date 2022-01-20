import random
print("Welcome to Hangman game!")

words=["Business","Portfolio","Adjustment"]

random_Selected_Word=random.choice(words)
To_fill_word=[]
To_fill=""
for i in range(len(random_Selected_Word)):
    To_fill_word.append("_")
    To_fill+="_ "


# print(To_fill)


print(f"Kindly start guessing for {To_fill}")
# UserInput=print("Enter a character to guess")