min_range = int(input("Enter the minimum range\n"))
max_range = int(input("Enter the maximum range\n"))

sum = 0
for number in range(min_range, max_range + 1):
    sum += number

print(f"the sum of numbers in range [{min_range} to {max_range}] is- {sum}  ")

print("\n==============================using steps==============\n")
steps = int(input("Enter the setps you want to take\n"))

sum = 0
for number in range(min_range, max_range + 1, steps):
    sum += number

print(f"the sum of numbers in range [{min_range} to {max_range} with steps {steps}] is- {sum}")
