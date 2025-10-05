"""
1) Takes two numbers as input from the user.

2) Performs the basic mathematical operations on these two numbers:
    o	Addition
    o	Subtraction
    o	Multiplication
    o	Division

3) Displays the results of each operation on the screen.
"""
print("--------------------------------------------------------------")

num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

add = num_1 + num_2
sub = num_1 - num_2
mul = num_1 * num_2
div = num_1 / num_2

print(" ")
print(f"The result for addition is: {add}")
print(" ")
print(f"The result for subtraction is: {sub}")
print(" ")
print(f"The result for multiplication is: {mul}")
print(" ")
print(f"The result for division is: {div}")
print(" ")
print("Thank you! Have a nice day!")
