get_all_height = input("Enter all the students heights (seperated by a space)\n").split()

for i in range(0, len(get_all_height)):
    get_all_height[i] = int(get_all_height[i])
print(get_all_height)
