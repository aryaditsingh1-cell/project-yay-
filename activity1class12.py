total_chores = 4
original_count = total_chores
print(f"Total chores to complete: {original_count}")

completed_count = 0
chore_num = 1
while chore_num <= total_chores:

    if chore_num == 1: next_chore = "walk the fish"
    elif chore_num == 2: next_chore = "make the house"
    elif chore_num == 3: next_chore = "eat the doors"
    elif chore_num == 4: next_chore = "wash the fish"
    else: next_chore = "break the table"
    answer = input(f"Have you completed chore {chore_num} ({next_chore})? (y/n): ")
    if answer == "y":
        completed_count += 1
    chore_num += 1

    print(f"Chores completed: {completed_count}")
else: 
    print("GO FINSIH YOUR CHORES")

    print(f"Total chores completed: {completed_count} out of {original_count}")
    print()

    print("YOUR CHORES ARE DONE")
    print("YOU ARE FREE TO GO\n")

    print("now lets look at what might possibly blow up your computer")
test_value = 0
saftey_counter = 0
while test_value < 0:
    print("this is a test to see if your computer can handle a while loop that never ends")
    test_value += 1
    saftey_counter += 1
    print(f"test value is: {test_value}")
    print(f"saftey counter is: {saftey_counter}")
    print(("lets stop or else we are blowing up"))
    break 

print("\nCHORE CHECKLIST")
print("CHORES ASSIGNED TODAY:", original_count)
print("CHORES COMPLETED TODAY:", completed_count)
print("CHORES REMAINING TODAY:", original_count - completed_count)
print("=======================================================================")
