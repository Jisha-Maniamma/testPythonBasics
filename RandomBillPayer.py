import random;
# import treasureHunt;
# To print randoms friends among friends who had dinner together and this friend will pay th bills of
# all the other friends too
names = input("Enter names of friends who had dinner [seperate them by a -,]").split(",")
random_Number = random.randint(0, len(names));

# print(names)

# print("name of restaurant is "+treasureHunt.Restaurant_name)
print(f"th randomly selected friend who would pay bill is- {names[random_Number]}")
