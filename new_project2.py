

operator = ["+", "-", "*", "/"]

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator not in operator:
    print("Invalid operator")
elif operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid operator")

print("The result is: " + str(result))


