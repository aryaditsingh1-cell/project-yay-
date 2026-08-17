# Grocery Billing Queue
 
print("=== GROCERY BILLING QUEUE :D PLEASE USE :) ===\n")
 
baby_price_items = 0
sort_of_big_price_items = 0
big_price_items = 0
 
customers_served = 0
total_sales = 0
 
billing = True
 
while billing:                              # outer while -- one customer per loop
    name = input("NAME: ")
    item_count = int(input(f"WHATS UPPPP {name} HOW MANY STUFF "))
 
    if item_count <= 0:
        print("WHAT NUMBER IS THIS\n")
        continue
 
    print(f"\nBILLING FOR ---> {name}:")
    customer_total = 0
    item_number = 1
 
    while item_number <= item_count:        # inner while -- one item per loop
        item_name = input("ITEM NAME: ")
        price = int(input("ITEM PRICE: "))
        quantity = int(input("QUANTITY: "))
 
        if price <= 0 or quantity <= 0:
            print("WRONG PRICE OR AMOUNT TYPE AGAIN.\n")
            continue
 
        item_total = price * quantity
        print(f"  {item_name}: {quantity} x {price} = {item_total}")
 
        customer_total += item_total
 
        if price < 50:
            baby_price_items += quantity
        elif price <= 100:
            sort_of_big_price_items += quantity
        else:
            big_price_items += quantity
 
        item_number += 1
 
    customers_served += 1
    total_sales += customer_total
 
    print(f"\nthis is the total for ---> {name}: {customer_total}")
    print("ALL DONE\n")
 
    again = input("NEXT (yes/no): ").strip().lower()
 
    if again != "yes":
        billing = False
 
 
print("\n=== gorcery sorting beep boop ===")
 
for slot in range(1, 4):                    # outer for -- one price category per loop
    if slot == 1:
        label, total = "baby price", baby_price_items
    elif slot == 2:
        label, total = "sort of big price", sort_of_big_price_items
    else:
        label, total = "big price", big_price_items
 
    if total > 0:
        print(f"  {label}: {total} ", end="")
 
        for item in range(total):           # inner for -- one symbol per item
            print("*", end="")
 
        print()
 
print(f"\nCustomers served : {customers_served}")
print(f"Total sales      : {total_sales}")
print("this grocery billing stand is closed go to another one")
