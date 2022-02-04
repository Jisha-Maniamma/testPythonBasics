#   Program to capitaliz ach starting word of your name
Firstname = input("Enter your first name  ").lower()
MiddleName = input("Enter our middle name  ").lower()
Lastname = input("Enter our last name  ").lower()


def capitalize(firstname, midddlename, Lastname):
    return firstname[0].upper() + firstname[1:len(firstname)] \
           + (" " + midddlename[0].upper() + midddlename[1:len(midddlename)] if midddlename != "" else "") \
           + " " + Lastname[0].upper() + Lastname[1:len(Lastname)]


print(capitalize(Firstname, MiddleName, Lastname))
