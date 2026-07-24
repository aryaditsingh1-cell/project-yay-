print("==SMART SCHOOL DAY PLANNER ==")
print ("Welcome to the Smart School Day Planner! This program will help you plan your school day based on the condition YOU answer. Please answer the following questions to get your personalized school day plan.")

day = input("What day of the week is it? (e.g., Monday, Tuesday, etc.): ").strip().capitalize()
weather = input("What the weather outside? (e.g., sunny, rainy, snowy, etc.): ").strip().lower()
homework = input("Do you have homework? (yes/no): ").strip().lower()

print()
print(f"SUMMARY OF YOUR SCHOOL DAY PLAN FOR {day}:")
print("-" * 100)

if day in ["Saturday", "Sunday"]:
    print("IT'S THE WEEKEND! NO SCHOOL TODAY. ENJOY YOUR DAY OFF!")
elif day == "Monday":
    print("IT'S MONDAY! TIME TO START THE WEEK STRONG. MAKE SURE TO GET YOUR HOMEWORK DONE AND STAY ORGANIZED.")
elif day == "Tuesday":
    print("IT'S TUESDAY! KEEP UP THE GOOD WORK. REMEMBER TO REVIEW YOUR NOTES AND PREPARE FOR ANY UPCOMING TESTS.")
elif day == "Wednesday":
    print("IT'S WEDNESDAY! YOU'RE HALFWAY THROUGH THE WEEK. STAY FOCUSED AND KEEP UP THE GOOD WORK.")
elif day == "Thursday":
    print("IT'S THURSDAY! YOU'RE GETTING THERE! STAY DETERMINED AND KEEP UP THE GOOD WORK.")
elif day == "Friday":
    print("IT'S FRIDAY! THE WEEK IS ALMOST OVER! STAY ORGANIZED AND PREPARE FOR THE WEEKEND.")
elif day == "summer vacation":
    print("IT'S SUMMER VACATION! ENJOY YOUR TIME OFF AND MAKE THE MOST OF YOUR SUMMER BREAK AND HOPE SCHOOL GETS DELAYED FOR A LONG TIME.")
else:
    print("what day are you talking about? I don't recognize that day. Please enter a valid day of the week.")

if weather == "sunny":
    print("IT'S SUNNY OUTSIDE! MAKE SURE TO WEAR SUNSCREEN AND STAY HYDRATED.")
elif weather == "rainy":
    print("IT'S RAINY OUTSIDE! DON'T FORGET TO BRING AN UMBRELLA AND WEAR WATERPROOF CLOTHING.")
elif weather == "snowy":
    print("IT'S SNOWY OUTSIDE! MAKE SURE TO DRESS WARMLY AND WEAR APPROPRIATE FOOTWEAR.")
elif weather == "cloudy":
    print("IT'S CLOUDY OUTSIDE! IT MIGHT BE A GOOD IDEA TO BRING A LIGHT JACKET JUST IN CASE.")
elif weather == "windy":
    print("IT'S WINDY OUTSIDE! MAKE SURE TO WEAR A WINDPROOF JACKET AND SECURE ANY LOOSE ITEMS.")
elif weather == "stormy":
    print("IT'S STORMY OUTSIDE! STAY SAFE AND AVOID GOING OUTSIDE IF POSSIBLE. MAKE SURE TO FOLLOW ANY WEATHER WARNINGS OR ADVISORIES AND MAYBE A POWER OUTAGE HAPPENS.")
elif weather == "foggy":
    print("IT'S FOGGY OUTSIDE! DRIVE CAREFULLY AND USE YOUR HEADLIGHTS. MAKE SURE TO STAY VISIBLE AND BE AWARE OF YOUR SURROUNDINGS.")
else:
    print("I DON'T RECOGNIZE THAT WEATHER CONDITION. PLEASE ENTER A VALID WEATHER CONDITION (e.g., sunny, rainy, snowy, etc.).") 
    if weather == "sunny" and homework == "yes":
        print("IT'S SUNNY AND YOU HAVE HOMEWORK! MAKE SURE TO BALANCE YOUR TIME BETWEEN ENJOYING THE WEATHER AND GETTING YOUR HOMEWORK DONE.")
    if weather == "sunny" and homework == "no":
        print("IT'S SUNNY AND YOU DON'T HAVE HOMEWORK! ENJOY THE WEATHER AND MAKE THE MOST OF YOUR FREE TIME.")
    if weather == "rainy" and homework == "yes":
        print("IT'S RAINY AND YOU HAVE HOMEWORK! MAKE SURE TO STAY DRY AND FOCUSED ON YOUR WORK.")
    if weather == "rainy" and homework == "no":
        print("IT'S RAINY AND YOU DON'T HAVE HOMEWORK! ENJOY THE WEATHER AND STAY DRY.")
    if weather == "snowy" and homework == "yes":
        print("IT'S SNOWY AND YOU HAVE HOMEWORK! MAKE SURE TO STAY WARM AND FOCUSED ON YOUR WORK.")
    if weather == "snowy" and homework == "no":
        print("IT'S SNOWY AND YOU DON'T HAVE HOMEWORK! ENJOY THE WEATHER AND STAY WARM.")
    if weather == "cloudy" and homework == "yes":
        print("IT'S CLOUDY AND YOU HAVE HOMEWORK! MAKE SURE TO STAY FOCUSED AND GET YOUR WORK DONE.")
    if weather == "cloudy" and homework == "no":    
        print("IT'S CLOUDY AND YOU DON'T HAVE HOMEWORK! ENJOY THE WEATHER AND MAKE THE MOST OF YOUR FREE TIME.")
    if weather == "windy" and homework == "yes":
        print("IT'S WINDY AND YOU HAVE HOMEWORK! MAKE SURE TO STAY FOCUSED AND GET YOUR WORK DONE.")
    if weather == "windy" and homework == "no":
            print("IT'S WINDY AND YOU DON'T HAVE HOMEWORK! ENJOY THE WEATHER AND MAKE THE MOST OF YOUR FREE TIME.")
    if weather == "stormy" and homework == "yes":
        print("IT'S STORMY AND YOU HAVE HOMEWORK! MAKE SURE TO STAY SAFE AND FOCUSED ON YOUR WORK.")
    if weather == "stormy" and homework == "no":
        print("IT'S STORMY AND YOU DON'T HAVE HOMEWORK! STAY SAFE AND MAKE THE MOST OF YOUR FREE TIME AND EXPECT OUTAGES JUST HOPE THERE ISNT A POWER OUTAGE.")
    if weather == "foggy" and homework == "yes":
        print("IT'S FOGGY AND YOU HAVE HOMEWORK! MAKE SURE TO STAY SAFE AND FOCUSED ON YOUR WORK.")
    if weather == "foggy" and homework == "no":
        print("IT'S FOGGY AND YOU DON'T HAVE HOMEWORK! STAY SAFE AND MAKE THE MOST OF YOUR FREE TIME.")

print("smart school day planner is now complete! Thank you for using the program. Have a great day and stay safe!")
print("Remember to check the weather and your homework assignments regularly to stay on top of your school day plan!")
print("Goodbye!")
print("This program was created by: ARYADIT")  # Replace [Your Name] with your actual name
print("==========================================")
    
    
  