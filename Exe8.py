__author__ = 'racattaque'

# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html:
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import time
import random
choices={1:"s",2:"p",3:"r"}

#2 players version
def RPS():
  player1=input("Player 1 name: ")
  player2=input("Player 2 name: ")
  print("Ok guys, let's play!")
  while True:
    choice1=input("%s, what s your choice (R for rock, S for Scissors and P for paper): " %player1)
    choice2=input("%s, what s your choice (R for rock, S for Scissors and P for paper): " %player2)
    if choice1.lower() not in choices.values() or choice2.lower() not in choices.values():
      print("Please give a valid selection")
      continue
    else:
      print("and the winner is...")
      time.sleep(1)
      if choice1.lower()=="r" and choice2.lower()=="s":
        print("the winner is %s" %player1)
      elif choice1.lower()=="s" and choice2.lower()=="p":
        print("the winner is %s" %player1)
      elif choice1.lower()=="p" and choice2.lower()=="r":
        print("the winner is %s" %player1)
      elif choice1.lower()==choice2.lower():
        print("It is a tie!")
      else:
        print("%s" %player2)
      if input("Do you wan to play again (Y/N)?").lower()=="n":
        break
  
  print("Thanks for playing, hope to see you soon...")
  
  
#one player version against computer.
def RPS_Alone():
  player1=input("Player 1 name: ")
  print("Hi %s , let's play!" %player1)
  while True:
    choice1=input("%s, what s your choice (R for rock, S for Scissors and P for paper): " %player1)
    if choice1.lower() not in choices.values():
      print("Please give a valid selection")
      continue
    else:
      choice2=random.randint(1,3)
      print("and the winner is...")
      time.sleep(1)
      if choice1.lower()=="r" and choices[choice2]=="s" or choice1.lower()=="s" and choices[choice2]=="p" or choice1.lower()=="p" and choices[choice2]=="r":
        print("%s" %player1)
      elif choice1.lower()==choices[choice2]:
        print("It is a tie!")
      else:
        print("artificial intelligence")
      if input("Do you wan to play again (Y/N)?").lower()=="n":
        break
  
  print("Thanks for playing, hope to see you soon...")

try:
  nbPlayer = int(input("Hi there, how many players (Max is 2)? "))
except:
  print("I said a number Grrrr\nCiao")
else:
  if nbPlayer==1:
    RPS_Alone()
  elif nbPlayer==2:
    RPS()
  elif nbPlayer==0:
    print("So you want me to play alone. No it does not work like that !")
  else:
    print("Sorry guys, I can t handle all of you at once")
