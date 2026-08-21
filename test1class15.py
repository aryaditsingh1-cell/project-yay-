secret = 42 
attempts = 5
hearts = 5
for heart in range(hearts):
    print("♥", end=" ")
    if attempts-1:
        print("You have", attempts, "attempts left.")
        if hearts == 0:
            print("hearts out the number was"+ secret)
while attempts > 0:
    guess = int(input("Guess the secret number: "))
    if guess > secret:
        print("you are cold")
    elif guess < secret:
        print("you are hot")
    elif guess == secret:
        print("you are on target!")
    else:
        print("Incorrect guess. Try again.")
        attempts -= 1
if attempts == 0:
    print("You've run out of attempts. The secret number was:", secret)


    




