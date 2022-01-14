print('''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')
print("Welcome to Treasure Island.")
print("You\'r mission is to find the treasure.")
direction_choice = input("choose 'left' or 'right'? \n").lower()
if direction_choice == 'left':
    Choice = input("do u want to 'swim' or 'wait'?\n").lower()
    if Choice=='swim':
        print('Game Over!')
    else:
        door = input("red Blue or yellow?\n").lower()
        if door=='yellow':
            print("you win")
        else:
            print("game Over!")
else:
    print("game Over!")
