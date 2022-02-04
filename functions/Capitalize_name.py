#   Program to capitaliz ach starting word of your name
Firstname = input("Enter your first name  ").lower()
MiddleName = input("Enter our middle name  ").lower()
Lastname = input("Enter our last name  ").lower()


def capitalize(firstname, midddleName, Lastname):
    return firstname[0].upper() + firstname[1:len(firstname)] \
           + (" " + midddleName[0].upper() + midddleName[1:len(midddleName)] if midddleName != "" else "") \
           + " " + Lastname[0].upper() + Lastname[1:len(Lastname)]


print(capitalize(Firstname, MiddleName, Lastname))
