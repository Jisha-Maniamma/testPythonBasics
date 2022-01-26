number = int(input("Enter your number to check as prime number "))


def prime_checker(num):
    for i in range(2, num):
        print(f"{num / i}")
        if (num % i) == 0:
            return "This is not prime"
            break;
    else:
            return "this is prime"





print(f"{prime_checker(num=number)}")
