# -----------------------
# Operations
# - Arithmatic cont.
# - Conditional statements
# - IF statements
# ------------------------

# ---
# Arithmatic
# ---

# Helpful to import the matplotlib and numply packages
import matplotlib.pyplot as plt
import numpy as np


# First define a variable
x = 2
print(x)

# Operators, +,1,*,/ are straight forward enough
x = x + 5 # note: the value of "x" has been reassigned
print(x)

# Augmented Assignment Operator: a way to more quickly assign calculations
x = 2
x += 5 # is identical to "x = x + 5" from above. Try using -=, *=, and /=.
print(x)

# Note that Python operates arithmetically according to the same order of operations in traditional mathematical operation.
y = 3;
x = y**3 # use the double asterisk to communicate a "power."
print (x)
# define pi
pi = np.pi
print(pi)
z = y**2 + (5+x) + 1 - pi
print(z)

# ---
# Operations
# ---
del x # to delete the value assignment to x previously

# Comparative operators
x = 3>2
print(x) # returns "true," since 3 is greater than 2

x = 3 == 2
print(x) # returns "false," since 2 and 3 are not equal

# other operators:
    #  !=, "not equal"
    #  ==, "equal"
    #  >, "greater than"
    #  >-, "greater than or equal to"
    #  <, "less than"
    #  <=, "less than or equal to"
# Each of these operations return a Boolean (true or false)

#-
# logical operations
#-

# these types of operations rely on the use of "or" and "and" statements.

# Examples
price = 50 # USD
print(price > 75 and price <60) # returns "False" since not both are true (only one condition is true)
print(price > 75 or price <60) # returns "True" since AT LEAST one of the conditions is true.

# using "not" to inerse the result
print(not price>40) # returns false, since false is the inverse of the true statement that the price is more than 40 USD.

# -
# IF statements
# -

# Use if to make a conditional statement/output
if price > 100:
    print("Can't afford this")
# remove the indention to terminate the statement

# One may add "else if" statements to adjust for other conditions.
if price > 100:
    print("That's way too much")
elif 49 < price < 100: # elif is the abbreviation for "else if"
    print("It's a bit of a stretch")
elif price < 48:
    print("I'll take it")
# Again, remove the indention to terminate the statement

#--------------
# End of lesson
#--------------