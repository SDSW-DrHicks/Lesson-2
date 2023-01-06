# ------------------------------------------------------
# Exercise #1: Guess the Secret Number
#-------------------------------------------------------

# Goal write a code which will prompt a guess from the user.
# If the guessed number equals the "secret" value the code will stop.
# If not, the prompt occurs again.

# Hint, use a while loop.

#-------------------------------------------------------
# KEY
#-------------------------------------------------------

secret_num = 6

guess = int(input("Guess a number, 1-10: "))

while guess != secret_num:
    print("Wrong. Try again.")
    guess = int(input("Guess a number, 1-10: "))

print("You win!")