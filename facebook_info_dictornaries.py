users = [
    {
        "name": "Mohan",
        "age":0,
        'friendsNumber': 0,
        'friendsName': [],
        'unreadMeassages': 0
    },
    {
        "name": "James",
        "age":0,
        'friendsNumber': 0,
        'friendsName': [],
        'unreadMeassages': 0
    }
]


def addUser(name, age, friendsNumber, friendsName, unreadMeassages):
    user_info = {}
    user_info["name"] = name
    user_info["age"] = age
    user_info["friendsNumber"] = friendsNumber
    user_info["friendsName"] = friendsName
    user_info["unreadMeassages"] = unreadMeassages
    users.append(user_info)


def updateUser(name, age, friendsNumber, friendsName, unreadMeassages):
    for thing in users:
        for a in thing:
            if thing[a] == name:
                thing["age"] = age
                thing["friendsNumber"]=friendsNumber
                thing["friendsName"]=friendsName
                thing["unreadMeassages"]=unreadMeassages



addUser(name="Ron", age=12, friendsNumber=100, friendsName=["aji", "shyam", "rahul", "Raju"], unreadMeassages=2)
print(users)
print("\n\n")
updateUser(name="Mohan", age=12, friendsNumber=100, friendsName=["aji", "shyam", "rahul", "Raju"], unreadMeassages=2)
print(users)
