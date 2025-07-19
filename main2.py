#Define functions for each operation
def add(a,b):
    return a + b
def subtract(a,b):
    return a-b
def multiply (a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "Error:Cannot divide by zero"
    return a / b
#Main program
print("Simple calculator")
print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter choice (1/2/3/4): ")
#Get numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# Perform selected operation
if choice == '1':
    result = add(num1, num2)
elif choice == '2':
    result = subtract(num1, num2)
elif choice == '3':
    result = multiply (num1, num2)
elif choice == '4':
    result = divide (num1, num2)
else :
    result = "INvalid input"
print ("Result:", result)    