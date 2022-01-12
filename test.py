print("hello world!")

age=int(input("your age?"))
# normal print statement
print("your age as entered "+str(age))
# formated string literals
print(f"your age is {age}")

if age>=18:
    print("you can search for jobs")
else:
    print("wait ... finish your studies")
