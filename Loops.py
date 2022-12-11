#---------------------------------
# Loops
#   - While loops
#   - Lists
#   - For loops
#---------------------------------

#---------------------------------
# While Loops
#---------------------------------

# Example 1: have a count from 1 to 10 printed in the console, without writing 10 print commands
i = 1
while i<11: # note, i is max'd out at 10, if I use 10, it'll stop counting at 9.
    print(i)
    i = i+1 # each time i is counted, it increase so that the loop will stop when it should.
# terminate the statement. See "operations" lesson for IF statements

# Example 2:
del i
i = 1
while i<11:
    print(i * '*')
    i = i+1
# run to see the difference between examples.

#-----------
# Lists
#-----------

# Lists are a collection of objects or values

names = ["Mason","Malachi","Nicholas","McCauley","Etahn"]
# Use commas to separate items in a list
print(names) # print the list
# Particular items in the list can be isolated using its index (refer to "operations" lesson).
print(names[0]) # This will print the zeroth (first) indexed item on the list.
# Python also allows for a "negative index." See example below:
print(names[-1]) # negative index returns the "first from the end" item.
# or
print(names[-2])
# Also an entire section of a list can be isolated.
print(names[0:3]) # This will return the zeroth, first, and second item BUT NOT THE THIRD.
# Note, none of the above prints have redefined the original list.

# items in a list can be used as variables
# For example, "Ethan" is misspelled. It can be corrected by:
names[4] = "Ethan" # the correct spelling will replace the current item.
print(names)

