def greet_customer():
    print("welcome one welcome all")
    print("take a drink or you will fall")

greet_customer()

price_per_cup = float(input("enter the price per cup in dollars"))
cups_sold = int(input("cups sold"))
def calculate_total(price,cup):
    total = price * cup
    return total
total_cost = calculate_total(price_per_cup,cups_sold)
rounded_total = round(total_cost,2 )
print("Total_cost:",rounded_total)
amount_paid=float(input("enter amount paid:"))
def calculate_change(paid , total):
    change = paid - total 
    return total 
change_due = calculate_change(amount_paid,rounded_total)
rounded_change = round(change_due,2)
    