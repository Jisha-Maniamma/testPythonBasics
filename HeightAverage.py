heights = input("Enter all the students heights (seperated by a space)\n").split()

for i in range(0, len(heights)):
    heights[i] = int(heights[i])
print(heights)

total_height = 0
total_length = 0
for height in heights:
    total_height += height
    total_length += 1

# using traditional for loop
print(f"average height is {str(round(total_height / total_length))}")

# using sum() and len() function
print(f"average height is {str(round(sum(heights) / len(heights)))}")
