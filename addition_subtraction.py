
# Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Display menu
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")

# User input for choice and numbers
choice = input("Enter choice (1/2): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operation and display result
if choice == '1':
    result = add(num1, num2)
    print(f"Result: {num1} + {num2} = {result}")
elif choice == '2':
    result = subtract(num1, num2)
    print(f"Result: {num1} - {num2} = {result}")
else:
    print("Invalid input. Please select a valid operation.")
