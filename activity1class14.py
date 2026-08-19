print("HALF PYRIMAID PATTERN OF STARS (*):")
n = int(input("Enter the number of rows for the half pyramid: "))
for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print()