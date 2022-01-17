
heights = input("Enter all the students heights (seperated by a space)\n").split()

for i in range(0, len(heights)):
    heights[i] = int(heights[i])
print(heights)

total_height=0
total_length=0
for height in heights:
    total_height+=height
    total_length+=1

print(f"average height is {str(round(total_height/total_length))}")


