temperature = int(input("Enter the temperature: "))
if temperature < 0:
    outfit = "It's freezing! Wear a heavy coat geez."
    print("GEEZ IT IS VERY COLD")
    print("WEAR A " + outfit + " OR YOU WILL BE SICK")
else:
    outfit = "It's not freezing! Wear a T shirt"
    print("IT'S NOT FREEZING")
    print("WEAR A " + outfit + " OR YOU WILL BE BOILING")

is_raining = input("IS IT RAINING? (yes/no): ")

if is_raining == "yes":
    print("BRING AN UMBRELLA OR YOU COMING HOME LIKE A SOGGY DOGGY")

wind_speed = int(input("WHAT IS THE WIND SPEED? (in mph): "))
if wind_speed > 20:
    print("IT'S WINDY! HOLD ON TO YOUR HAT OR IT GOES BYE BYE")
else:
    print("IT'S NOT WINDY! YOU CAN WEAR YOUR HAT WITHOUT WORRYING")

if has_puddles := input("ARE THERE PUDDLES? (yes/no): ") == "yes":
    shoes = "RAINBOOTS"
    print("WATCH OUT FOR PUDDLES OR YOU WILL GET WET FEET")
else:
    shoes = "SNEAKERS"
    print("NO PUDDLES! YOU CAN WEAR YOUR SNEAKERS WITHOUT WORRYING")

print("")
print("SUMMARY OF WEATHER CONDITIONS:")
print(f"Temperature: {temperature}°C")
print(f"Is it raining? {is_raining}")
print(f"Wind speed: {wind_speed} mph")
print(f"Are there puddles? {has_puddles}")
print(f"Recommended shoes: {shoes}")
print(f"Recommended outfit: {outfit}")
print("STAY SAFE AND DRESS APPROPRIATELY FOR THE WEATHER!")
print("THANK YOU FOR USING THE WEATHER ADVISOR PROGRAM!")
print("HAVE A GREAT DAY AND STAY WARM OR COOL, WHATEVER THE WEATHER MAY BE!")
print("REMEMBER TO CHECK THE WEATHER REGULARLY AND DRESS ACCORDINGLY!")
print("GOODBYE!")