proramming_Dicitonary = {
    "Bug": "An error",
    "Function": "a piece of code"

}

print(proramming_Dicitonary["Bug"])
######## add new entry and change entry
proramming_Dicitonary["loop"] = "over and over again"
proramming_Dicitonary["Bug"] = "again and again"
print(proramming_Dicitonary)

a = {}
proramming_Dicitonary = {}
print(proramming_Dicitonary)
######## ahange or add new
proramming_Dicitonary["Bug"] = "again and again"
print(proramming_Dicitonary)

######## acess full irctory
for thing in proramming_Dicitonary:
    print(thing)
    print(proramming_Dicitonary[thing])