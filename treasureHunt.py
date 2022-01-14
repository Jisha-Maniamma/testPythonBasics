print("welcome to Treasure island. Your mission is to find treasure")
direction_choice = input("choose left or right? \n").lower()
if direction_choice == 'right':
    print("Game Over")
else:
    Choice = input("swim or wait?\n").lower()
    if Choice=='swim':
        print('Game over')
    else:
        door = input("red Blue or yellow?\n").lower()
        if door=='yellow':
            print("you win")
        else:
            print("game Over")
