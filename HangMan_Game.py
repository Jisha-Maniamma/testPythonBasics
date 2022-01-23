import random

print("Welcome to Hangman game!")
# business portfolio
words = ["buus", "poprt", "adjustament"]

random_Selected_Word = random.choice(words)
To_fill_word = []
To_fill = ""
for i in range(len(random_Selected_Word)):
    To_fill_word.append("_")
    To_fill += "_ "

# print(To_fill)


print(f"Kindly start guessing for {To_fill} {To_fill_word}")

while not (To_fill_word.count('_')==0):
    UserInput = input("Enter a character to guess").lower()
    for position in range(len(random_Selected_Word)):
      if random_Selected_Word[position] == UserInput:
        To_fill_word[position] = UserInput
    # print(f"correct  ")
        print(f"Kindly start guessing for  {To_fill_word}")


