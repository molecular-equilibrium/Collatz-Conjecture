# The Collatz conjecture:
# A mathematical hypothesis that states for any number,
# it will eventually reach down to the number one
# using a sequence followed by a given set of rules.

# If the number is even, divide by 2.
# If the number is odd, multiply 3 and add 1.
# The sequence will eventually reach 1 according
# to the hypothesis, but no one has yet to disprove
# the hypothesis is incorrect.

# Starting integer.
given_number = 290

while True:
  # Loop begins with the given_number
  # to display the sequence.
  print(int(given_number))
  if given_number % 2 == 0:
    # Number is even.
    # Divide number.
    divide = given_number / 2

    # Change variable to that
    # quotient.
    given_number = divide

    # Loop repeats after this block
    # is done executing.

  elif given_number == 1:
    # If given_number is 1, break loop.
    break

  elif given_number < 1:
    # Hypothesis incorrect in this case.
    # If a number is even found to exist, this
    # block will execute.
    print('Collatz was wrong!')
    break

  else:
    # All else, multiply odd number by 3 and add 1
    multiply = given_number * 3 + 1

    # Change variable to that sum
    given_number = multiply