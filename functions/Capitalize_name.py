#   Program to capitaliz ach starting word of your name
Firstname = input("Enter your first name  ").lower()
MiddleName = input("Enter our middle name  ").lower()
Lastname = input("Enter our last name  ").lower()


def capitalize(firstname, midddlename, lastname):
    if firstname == "" and midddlename == "" and lastname == "":
        return "you didnot provide valid inputs!"
    return firstname[0].upper() + firstname[1:len(firstname)] \
           + (" " + midddlename[0].upper() + midddlename[1:len(midddlename)] if midddlename != "" else "") \
           + " " + lastname[0].upper() + f"{lastname[1:len(lastname)]}"


print(capitalize(Firstname, MiddleName, Lastname))
