import random;
# To print randoms friends among friends who had dinner together and this friend will pay th bills of
# all the other friends too
names = input("Enter names of friends who had dinner [seperate them by a -,]").split(",")
random_Number = random.randint(0, len(names));

# print(names)

print(f"th ransomly selected frind who would pay bill is- {names[random_Number]}")
