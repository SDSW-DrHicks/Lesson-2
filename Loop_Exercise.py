#------------------------------------------------------------------------------------
# Exercise #1: IF Statements and FOR Loops
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
# Task: Write a program which will calculate the factorial of any integer input:
# Remember:
# - For negative numbers, remember that the factorial does not exist.
# - The factorial of zero is 1.
# - The factorial of a positive number, such as 5, is = 5*4*3*2*1 = 120.
# The code should include:
# - IF statements
# - An input prompt
# - A FOR Loop
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
# Key
#------------------------------------------------------------------------------------

# Write a line asking for a value from the user.
num = input("For what integer would you like to know the factorial? ")
# avoid using "int" for "integer" except when converting input types to not confuse.

# Define the initial factorial value.
factorial = 1

# The factorial of a negative number does not exist
if int(num) < 0:
    print("Factorial does not exist for negative numbers")
# The factorial of zero is 1.
elif num == 0:
    print("The factorial of 0 is 1")
# Calculate the factorial of any positive integer:
else:
    for i in range(1, int(num)+1):
# 1 is added to the upper limit of the range since the indexes of the range are not the actual values being calculated.
# multiply factorial by current number
        factorial = factorial * i
# This line calculates factorials based on each successive multiple of "i."
    print("The factorial of", num, "is", factorial)
# Print the solution to the factorial.

#------------------------------------------------------------------------------------
# End of code
#------------------------------------------------------------------------------------