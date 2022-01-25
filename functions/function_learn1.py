def greet(name, age, height):
    print(f"hai there {name} with age- {age} and height {height}, this is jisha!")


for i in range(0, 3):
    name = "a" + str(i)
    greet(name=name, height=150 + i, age=(20 + i))
