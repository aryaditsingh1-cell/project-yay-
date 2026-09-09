def calculate_change(paid,price):
    change = paid - price
    return change
snack_price = 2.00
drink_price = 1.50
print("======SNACK MACHINE======")
print(f"Snack price: ${snack_price} money")
print(f"Drink price: ${drink_price} money")
print("THESE COINS THAT ARE VERY NICE: $1, $5, $10, $20")

total_inserted = 0
coins_inserted = 0
drink_list = ["", "gatorade", "redbull", "monster", "fanta", "sprite", "drpepper", "mountaindew", "peachsnapple", "applejuice", "orangejuice", "grapefruitjuice", "water", "milk", "chocolatemilk", "icedtea", "lemonade", "fruitpunch", "coconutwater", "sparklingwater", "energywater", "vitaminwater", "kombucha", "seltzer", "club soda", "ginger ale", "root beer", "cream soda", "cola", "diet cola", "diet root beer"]
food_list = ["", "chips", "candybar", "cookies", "crackers", "popcorn", "pretzels", "nuts", "trail mix", "granola bar", "fruit snacks", "mystery", "cheese sticks", "yogurt", "pudding cups", "fruit cups", "applesauce cups", "rice cakes", "waffles", "muffins, lays", "doritos", "candy corn", "gummy bears", "sour patch kids", "twizzlers", "skittles", "m&ms", "snickers", "kitkat"]
drink_choice = input(f"Please choose an item from the following list: {drink_list}: ")
food_choice = input(f"Please choose an item from the following list: {food_list}: ")
if food_choice not in food_list:
    print("INVALID FOOD CHOICE")
    exit()
if drink_choice not in drink_list:
    print("INVALID DRINK CHOICE")
    exit()

while True:
    coin = int(input("Insert coin (enter 0 to finish): "))

    if coin != 1 and coin != 5 and coin != 10 and coin != 20:
        print("BAD COIN PUT ANOTHER COIN")
        continue
    total_inserted += coin
    coins_inserted += 1
    print(f"COINS THAT WERE TAKEN: {coins_inserted} TOTAL AMOUNT INSERTED: ${total_inserted}")

    if total_inserted >= drink_price:
        print("YOU HAVE INSERTED ENOUGH MONEY")
        break
change_due = calculate_change(total_inserted, drink_price)
print("uh beep boop beep beep")
if change_due == 0:
        pass
else:
        print(f"HEY WAIT FOR YOUR CHANGE: ${change_due}")

print("\n=======================VENDING SUMMARY BOOP BEEP=======================")
print("drink price: $", drink_price)
print("snack price: $", snack_price)
print("total amount inserted: $", total_inserted)
print("change due: $", change_due)
print("food choice: ", food_choice)
print("drink choice: ", drink_choice)
print("thank you for using the vending machine, have a nice day!")
print("======================================================================")
