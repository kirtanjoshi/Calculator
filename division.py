def divide(a, b):
    return "Error: Division by zero" if b == 0 else a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = divide(num1, num2)
print("Result:", result)
