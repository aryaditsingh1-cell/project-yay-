rowsize = int(input("Enter the number of rows"))
if rowsize%2 == 0:
    halfdiam = int(rowsize/2)
else:
    halfdiam = int(rowsize/2)+1
    space = halfdiam - 1
    for i in range(1, halfdiam+1):
        for j in range(1, space+1):
            print(" ", end="")
        space -= 1
        for j in range(1, 2*i):
            print("*", end="")
        print()