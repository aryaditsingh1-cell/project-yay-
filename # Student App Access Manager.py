# Student App Access Manager
 
# Permission values stored as binary bits
CAMERA = 1       # 0001
MICROPHONE = 2   # 0010
STORAGE = 4      # 0100
LOCATION = 8     # 1000
 
# List of apps available to students
approved_apps = [
   "gaming app",
       "shopping app",
       "social media app"
        "fun app"
        "coding app"
]
 
# Get student details
student_name = input("Enter your name: ")
requested_app = input("Enter the app you want to access: ").lower()
 
print("\n--- Identity Operator Check ---")
 
# Use 'is' to check the data type
if type(student_name) is str:
    print("THIS PERSON APP IS STORED.")
 
# Use 'is not' to check the data type
if type(requested_app) is not int:
    print("THIS APP ISNT AN APP.")
 
 
print("\n---THE MEMBERSHIP APP---")
 
# Use 'in' to check whether the app is approved
if requested_app in approved_apps:
    print(requested_app, "is an approved student app.")
else:
    print(requested_app, "is not an approved student app.")
 
# Use 'not in' to check restricted apps
restricted_apps = [
    "math app"
    "science app"
    "learning apps"
    
]
 
if requested_app not in restricted_apps:
    print("THIS APP ISNT RESTRICTED, HAPPY PLAYING")
else:
    print("BOOOOOOOO")
 
 
print("\n--- App Permission Settings ---")
 
# Combine permissions using the bitwise OR operator
student_permissions = CAMERA | MICROPHONE | STORAGE
 
# Display the permission number in binary
print("Permission value:", student_permissions)
print("Permission bits:", bin(student_permissions))
 
# Check permissions using the bitwise AND operator
if student_permissions & CAMERA:
    print("CAMERA ENABLED")
 
if student_permissions & MICROPHONE:
    print("MIC ENABLED")
 
if student_permissions & STORAGE:
    print("STORAGE USAGE ENABLED")
 
if student_permissions & LOCATION:
    print("LOCATION USAGE ENABLED")
else:
    print("LOCATION DISABLED")
 
 
print("\n--- bit shift demonstration---")
 
# Shift the CAMERA bit left to create the next permission value
next_permission = CAMERA << 1
 
print("Camera bit:", bin(CAMERA))
print("After left shift:", bin(next_permission))
 
# Shift the STORAGE bit right
previous_permission = STORAGE >> 1
 
print("Storage bit:", bin(STORAGE))
print("After right shift:", bin(previous_permission))
 
 
print("\n--- Final Access Result ---")
 
# Check both app approval and permission availability
if requested_app in approved_apps and requested_app not in restricted_apps:
    print("Access granted to", requested_app)
else:
    print("Access denied to", requested_app)

