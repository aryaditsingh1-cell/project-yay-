# Homework Completion Tracker
 
# PART 1: Set today's total number of homework tasks
total_homework = 4
original_count = total_homework
print(f"You have {original_count} homework tasks to finish today!\n")
 
# PART 2: Keep a counter for completed homework and the current task number
completed_count = 0
task_num = 1
 
# PART 3: Repeat while there are still homework tasks left
while task_num <= total_homework:
 
    # PART 4: Work out the current homework task from its number
    if task_num == 1:
        next_task = "finding pi ☠️☠️☠️"
    elif task_num == 2:
        next_task = "finding the theory of relativity "
    elif task_num == 3:
        next_task = "writing a wild essay"
    else:
        next_task = "making very crazy codes"
 
    answer = input(f"Have you finished: {next_task}? (yes/no): ")
 
    # PART 5: Only move on once the task is marked done
    if answer == "yes":
        completed_count += 1
        task_num += 1
        print("nice you have no homework left")
    else:
        print("go finish it right now")
 
    # PART 6: Print how many homework tasks remain
    print("homework remaining:", total_homework - completed_count)
    print()
 
# PART 7: This only prints once every homework task is marked done
print("===== ALL HOMEWORK COMPLETE! =====")
print("nice your homework is done\n")
 
# PART 8: A safe look at what an infinite loop would look like
print("Now lets make our computer scream")
test_value = 0
safety_counter = 0
 
while test_value <= 0:
    print("we can blow up a pc with this")
    safety_counter += 1
 
    if safety_counter == 3:
        print(("but lets not "))
        break
 
# PART 9: Print the final homework checklist summary
print("\n===== HOMEWORK COMPLETION SUMMARY =====")
print("Homework Assigned Today:", original_count)
print("Homework Completed:", completed_count)
print("Homework Remaining:", total_homework - completed_count)
print("=======================================")
