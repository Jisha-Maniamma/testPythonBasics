Firstname = input("Enter your first name  ").lower()
Lastname = input("Enter our last name  ").lower()


def capitalize(Firstname, Lastname):
    return Firstname[0].upper() + Firstname[1:len(Firstname)] + " " + Lastname[0].upper() + Lastname[1:len(Lastname)]


print(capitalize(Firstname, Lastname))
