def add_number(a, b):
    """Returns the sum of two numbers."""
    return a + b
def subtract_number(a, b):
    """Returns the difference of two numbers."""
    return a - b
def multiply_number(a, b):
    """Returns the product of two numbers."""
    return a * b
def divide_number(a, b):
    """Returns the quotient of two numbers. Raises ValueError if b is zero."""
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    except (ValueError) as e:
        print(f"Error: {e}")
        return None
value = float(input("Enter a number to find all 4 basic operations with it): "))
result = add_number(value, 10), subtract_number(value, 10), multiply_number(value, 10), divide_number(value, 10)
print(result)

