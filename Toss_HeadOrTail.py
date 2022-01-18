import random;

print("Starting to toss...")
random_number = random.randint(0, 1)
if random_number == 1:
    print("you got a Head...you Win!!")
else:
    print("you got a Tail...you loose!")
