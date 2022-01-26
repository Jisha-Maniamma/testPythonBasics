coverage = 5

height = int(input("Enter the height of your wall  "))
width = int(input("Enter the width of your wall  "))


def PaintCanCalculator(height, width):
    return (height * width) / coverage


print(f"You would need no of cans : {round(PaintCanCalculator(height=height, width=width))}")
