number = input("Enter the numbers [with space]\n").split()

for i in range(0, len(number)):
    number[i] = int(number[i])

print(number)
max_number = 0
for num in number:
    print(f"{max_number} and {num}")
    if max_number < num:
        max_number = num

print(f"Maximum number is {max_number}")
