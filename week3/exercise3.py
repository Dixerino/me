"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
  
    isnumber = False

    # Inputting bounds; whilst making sure it is number
    print("\nWelcome to the guessing game!")
    while not isnumber:
      try:
        lower = str((input("Enter a lower bound: ")))
        upper = str(input("Enter an upper bound: "))
        upperBound = int(upper)
        lowerBound = int(lower)
        print("OK then, a number between " + lower + " and " + upper + "?")
        isnumber = True
      except ValueError:
        print('Not proper numbers; Enter bounds again!')

    # Number Generator
    actualNumber = random.randint(lowerBound, upperBound)

    ## while loop for the actual guessing
    # Setting guessed status as False to begin
    guessed = False

    while not guessed:
      try:
        guess = str(input('Guess a Number: '))
        guess = int(guess)
        if guess < lowerBound:
          print("Too low, ho")
        elif guess > upperBound:
          print("You're out of the bounds buddy")
        else:
          if guess == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = True
          elif guess < actualNumber:
            print('Too low, GUESS AGAIN')
          else:
            print('Too high, GUESS AGAIN')
      except ValueError:
        print('Not a proper number; Guess a Number again!')
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
