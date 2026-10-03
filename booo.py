# ================================
# FUNCTION CALCULATOR
# ================================

# ---------- PART 1: four functions ----------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# ---------- MAIN PROGRAM (given to you) ----------
print("FUNCTION CALCULATOR")

# ---------- PART 2, 3 and 4: input, choose, errors ----------
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    if operation == "add":
        result = add(num1, num2)
        print("Result:", result)
    elif operation == "subtract":
        result = subtract(num1, num2)
        print("Result:", result)
    elif operation == "multiply":
        result = multiply(num1, num2)
        print("Result:", result)
    elif operation == "divide":
        result = divide(num1, num2)
        print("Result:", result)
    else:
        print("Unknown operation.")
except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Thank you for using the FUNCTION CALCULATOR.")
