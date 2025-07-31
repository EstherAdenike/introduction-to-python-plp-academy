# Basic Calculator Program

# Ask the user to input two numbers
first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))

# Ask the user to input the mathematical operation
maths_operator = input("Enter the operation (+, -, *, /): ")

if maths_operator == '+':
    result = first_num + second_num
    print(f"{first_num} + {second_num} = {result}")
elif maths_operator == '-':
    result = first_num - second_num
    print(f"{first_num} - {second_num} = {result}")
elif maths_operator == '*':
    result = first_num * second_num
    print(f"{first_num} * {second_num} = {result}")
elif maths_operator == '/':
    if second_num!= 0:
        result = first_num / second_num
        print(f"{first_num} / {second_num} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please use +, -, *, or /.")   

      