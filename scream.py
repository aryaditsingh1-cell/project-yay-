# ================================
# SHOPPING DISCOUNT CALCULATOR
# ================================

# ---------- PART 1: retry loop ----------
valid = False
while not valid:
    try:
        bill = float(input("Enter the bill amount: "))
        discount_percent = float(input("Enter the discount percent: "))
        num_people = int(input("Enter the number of people: "))

        discount_amount = bill * (discount_percent / 100)
        final_bill = bill - discount_amount
        per_person = final_bill / num_people

    except ValueError:
        print("Error: Please type numbers only.")
    except ZeroDivisionError:
        print("Error: Number of people cannot be 0.")
    else:
        print("Final bill after discount:", final_bill)
        print("Each person pays:", per_person)
        valid = True
    finally:
        print("Attempt finished.")

