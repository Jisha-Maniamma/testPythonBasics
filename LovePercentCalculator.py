#
# Author- Jisha Maniamma
# To check your compatibility with your partner in percentage
#
first_name = input("enter the first name \n").lower()
second_name = input("enter the second name \n").lower()

fullname = first_name + second_name
l = fullname.count('l')
o= fullname.count('o')
v= fullname.count('v')
e= fullname.count('e')
t= fullname.count('t')
r= fullname.count('r')
u= fullname.count('u')
e= fullname.count('e')
score=str(t+r+u+e)+str(l+o+v+e)
print(f" {first_name} and {second_name} , your compatibility is {score}")

score=int(score)
if score<10 or score>90:
    print()
elif score>=40 or score<=50:
    print(f"you score is {score}, you go together like coke and mentos")
else:
    print(f"you score is {score}, you are alright togethe")
