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

# Augmented Assignment Operator: a way to more quickly perform calculations
x = 2
x = 5 # is identical to "x = x + 5" from above. Try using -=, *=, and /=.
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
# Conditionals
# ---

