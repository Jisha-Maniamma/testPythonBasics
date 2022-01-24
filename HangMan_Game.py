import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print("Welcome to Hangman game!")
# business portfolio
words = ["bus", "port", "adjustment"]

random_Selected_Word = random.choice(words)
To_fill_word = []
To_fill = ""
for i in range(len(random_Selected_Word)):
    To_fill_word.append("_")
    To_fill += "_ "

# print(To_fill)
# life available
Player_life = 6

print(f"Kindly start guessing for {To_fill} {To_fill_word}")

###############################################
#          SOLUTION-1
###############################################
# while not (To_fill_word.count('_')==0):
#     UserInput = input("Enter a character to guess").lower()
#     for position in range(len(random_Selected_Word)):
#       if random_Selected_Word[position] == UserInput:
#         To_fill_word[position] = UserInput
#       else:
#         print("sorry enter letter again")
#     # print(f"correct  ")
#         print(f"Kindly start guessing for  {To_fill_word}")

###############################################
#            SOLUTION-2
###############################################
end_of_game = False;
while not end_of_game:
    UserInput = input("Enter a character to guess").lower()
    for position in range(len(random_Selected_Word)):
        if random_Selected_Word[position] == UserInput:
            To_fill_word[position] = UserInput
        else:
            Player_life -= 1

    if '_' not in To_fill_word:
        end_of_game = True;
    if Player_life == 0:
        end_of_game = True;

    print(f"Kindly start guessing for  {To_fill_word}")
