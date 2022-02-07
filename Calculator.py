def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


# operator dictonary
operator = {}
operator["+"] = add
operator["-"] = sub
operator["*"] = mul
operator["/"] = div


# print(operator)
def calculatorMain():
    num1 = float(input("Enter the first number "))

    choice = "y"
    while choice == "y":
        num2 = float(input("Enter the Second number "))
        print("which of the operation do you wnt to do")
        for op in operator:
            print(op)
        symbol_selected = input("select the symbol  ")
        calculator = operator[symbol_selected]
        answer = calculator(num1, num2)
        print(f"{num1}{symbol_selected}{num2}={answer}")
        choice = input("type 'y' to continue using the last result")
        if choice != 'y':
            calculatorMain()
        else:
            num1 = answer


calculatorMain()
