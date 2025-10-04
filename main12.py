def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

#printing the inputs from the user
print("Please select operation")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter your choice(a/b/c/d)")

num1 = int(input("please enter your first number"))
num2 = int(input("please enter your second number"))

if choice == "a":
    print(num1, "+" , num2 , "=", add(num1,num2))
if choice == "b":
    print(num1, "-" , num2 , "=", Subtract(num1,num2))
if choice == "c":
    print(num1, "*" , num2 , "=", multiply(num1,num2))
if choice == "d":
    print(num1, "/" , num2 , "=", divide(num1,num2))
else:
    print("Invalid input")