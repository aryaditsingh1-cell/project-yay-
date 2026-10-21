# ================================
# STUDENT GRADE BOOK
# ================================

# ---------- PART 1: the dictionary ----------
# YOUR CODE HERE
# Make a dictionary called grades with five students.
# Each key is a name and each value is a score.

# ---------- PART 2: class average ----------
# YOUR CODE HERE
# Make total = 0. Loop over grades and add each score to total.
# Divide total by len(grades) and print the class average.

# ---------- PART 3: highest score ----------
# YOUR CODE HERE
# Make top_name = "" and top_score = 0.
# Loop over grades. If a score is higher than top_score,
# save that name in top_name and that score in top_score.
# Print the highest scorer and the score.

# ---------- PART 4: look up a student ----------
# YOUR CODE HERE
# Ask for a student name with input().
# Print the score with .get(). Use "Not found" if the name is not in grades.
grade_book = {"Bob": 85, "Alice": 92, "Charlie": 78, "David": 90, "Eve": 88, "Rob": 95}
total = 0
for name in grade_book:
    total = total + grade_book[name]
class_average = total / len(grade_book)
print("Class average:", class_average)
top_name = ""
top_score = 0
for name in grade_book:
    if grade_book[name] > top_score:
        top_name = name
        top_score = grade_book[name]
print("Highest scorer:", top_name, "with score:", top_score)
lookup_name = input("Enter a student name: ")
print(grade_book.get(lookup_name, "Not found"))


