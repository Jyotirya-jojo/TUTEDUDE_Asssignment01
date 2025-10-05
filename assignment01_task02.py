"""
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
"""
print("--------------------------------------------------------------")

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

full_name = f"{first_name} {last_name}"

print("")
print(f"Nice to meet you, {full_name}! Have a nice day!")
