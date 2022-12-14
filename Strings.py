#-----------------------------
# Strings
#-----------------------------

# Strings are a type of non-numberical data in programs.

# Let's create a variable with a string value assignment:
course = "Intro to Programming"
# index-> 01234
# Strings, and characters within strings have an index number which could be used
# to identify segments or parts of the string. In the case above, "Intro..." is indexed with a number for each
# character, beginning with 0. So, "I" is 0, "n" is 1, "t" is 2... and so forth.


# Use this line to print the uppercase "self" of the variable "course."
print(course.upper())
print(course.lower())

# Using the index, one can identify specific parts of the string.
print(course.find('t'))
# After running, the output of "2" should be displayed.

print(course.replace('to','2'))
# This replaces a prat of the string. However, it does not overwrite the value
# assigned to "course."

