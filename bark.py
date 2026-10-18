items = ["pencil", "eraser", "notebook", "markers", "crayons"]
stock = [600, 0, 150, 0, 100]
stuff_that_we_have = {item: count for item, count in zip(items, stock)}
print("we have this stuff", stuff_that_we_have)
in_the_store = [item for item in items if stuff_that_we_have[item] > 0]
print("items in the store are", in_the_store)
out_of_stock = [item for item in items if stuff_that_we_have[item] == 0]
print("items out of stock are", out_of_stock)
what_they_want = input("what do you want")
if what_they_want not in stuff_that_we_have or stuff_that_we_have[what_they_want] == 0:
    print(what_they_want, "is not available now shoo")
    exit()

prices = [4386,634827,3428,326,43234432]
markup = int(input("enter the markup for the stuff: "))
markup_price = list(map(lambda price: price + markup, prices))
print("prices after markup are", markup_price)
item_index = items.index(what_they_want)
thing_price = markup_price[item_index]
print("the price for", what_they_want, "after markup is", thing_price)
stuff_that_we_have[what_they_want] = stuff_that_we_have[what_they_want] - 1
print("updated stock for", what_they_want, "is", stuff_that_we_have[what_they_want])
print(what_they_want,"is now in your hands whats laft of it is", stuff_that_we_have[what_they_want])
if stuff_that_we_have[what_they_want] == 0:
    print(what_they_want, "is now out of stock")
    out_of_stock.append(what_they_want)
    in_the_store = [item for item in items if stuff_that_we_have[item] > 0]
    print("items in the store are", in_the_store)
    print("items out of stock are", out_of_stock)
else:
    print(what_they_want, "is still in stock")
    print("items in the store are", in_the_store)
    print("items out of stock are", out_of_stock)
    print("")
    print("store is now closed")
    print("thing bought is", what_they_want)
    print("price paid is", thing_price)
    print("remaining stock for all items is", stuff_that_we_have)
    print("thank you for shopping with us!")
    