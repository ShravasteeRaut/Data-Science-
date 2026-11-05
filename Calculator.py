def add(num1, num2):
    return(num1 + num2)

def subtract(num1, num2):
    return(num1 - num2)

def multiply(num1, num2):
    return(num1 * num2)

def divide(num1, num2):
    return(num1 / num2)

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
print("a = Add\t b = Subtract\t c = Multiply\t d = Divide")
opperator = input("Enter the form of operator from the options above: ")


if opperator == "a":
  print(add(num1, num2))

if opperator == "b":
  print(subtract(num1, num2))

if opperator == "c":
  print(multiply(num1, num2))

if opperator == "d":
  print(divide(num1, num2))



