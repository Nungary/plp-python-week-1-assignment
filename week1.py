#code to ask user to input first and second number 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#code to ask user to input the operation of choice
operation = input("enter the operation (+, -, *, /):")

#code to perfom the operation based on user's input and print the result


if operation == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == '/':
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("invalid operation")
    