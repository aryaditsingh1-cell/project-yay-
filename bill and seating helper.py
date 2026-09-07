# Bill & Seating Helper
 
# PART 1: Define a function using positional arguments
def total_bill(bill_amount, tip_perc):
    # Calculate final bill after adding tip
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f"PAY UP PAY UP OR YOU A DUCK ${total}")
    return total
 
# PART 2: Call the function with positional arguments
total_bill(150, 20)
 
 
# PART 3: Define a recursive function with a docstring
def seating_arrangements(guests):
    '''This is a recursive function to find the number of seating arrangements for guests.'''
 
    # Base case
    if guests == 0 or guests == 1:
        return 1
 
    # Recursive case
    else:
        return guests * seating_arrangements(guests - 1)
 
 
# PART 4: Access and print the docstring
print(seating_arrangements.__doc__)
 
# PART 5: Display seating arrangement results
print("SEATS FOR 1 GUEST:", seating_arrangements(1))
print("SEATS FOR 2 GUESTS:", seating_arrangements(2))
print("SEATS FOR 3 GUESTS:", seating_arrangements(3))
print("SEATS FOR 5 GUESTS:", seating_arrangements(5))
