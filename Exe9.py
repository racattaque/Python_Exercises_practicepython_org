__author__ = 'racattaque'

# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user want to stop
# Keep track of how many guesses the user has taken, and when the game ends, print this out.


import random
numberGuess=0
numberOfGames=0
newGame=True
while True:
  try:
    guess=int(input("Guess a number"))
    numberGuess+=1
  except:
    print("I said a number, what s wrong with you ?")
    continue
  if newGame:
    num=random.randint(1,9)
    numberOfGames+=1
    newGame=False
  if num==guess:
    print("That s it. You had %d guesses to get it" %numberGuess)
    answer=input("do you want to keep playing (Y/N)?")
    if answer.lower()=="y":
      newGame=True
      continue
    else:
      break
  elif num>guess:
    print("That s too low, try again")
    continue
  else:
    print("That s too high, try again")
    continue
chance=round(numberOfGames/numberGuess*100.0,2)
print("Thanks for playing. You are %s lucky today." %(chance))
