def greet(name, age, height):
    print(f"hai there {name} with age- {age} and height {height}, this is jisha!")


for i in range(0, 3):
    name = "a" + str(i)
    greet(name=name, height=150 + i, age=(20 + i))

# hai there a0 with age- 20 and height 150, this is jisha!
# hai there a1 with age- 21 and height 151, this is jisha!
# hai there a2 with age- 22 and height 152, this is jisha!
