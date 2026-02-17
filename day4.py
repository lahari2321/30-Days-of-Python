print("Welcome to the Simple Calculator!...")
num1=int(input("Enter a number1:--"))
num2=int(input("Enter a number2:--"))


operation=input("Enter an operator (+, -, *, /): ")

if operation == '+':
    print(f"Addition of {num1} and {num2} is {num1 + num2}")
elif operation == '-':
    print(f"Subtraction of {num1} and {num2} is {num1 - num2}")
elif operation == '*':
    print(f"Multiplication of {num1} and {num2} is {num1 * num2}")
elif operation == '/':
    if num2 != 0:
        print(f"Division of {num1} and {num2} is {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
        result = None

else:
    print("Invalid operator. Please use +, -, *, or /.")