__author__ = 'racattaque'

# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html:
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import time
import random

#2 players version
def RPS():
  player1=input("Player 1 name: ")
  player2=input("Player 2 name: ")
  print("Ok guys, let's play!")
  while True:
    choice1=input("%s, what s your choice (R for rock, S for Scissors and P for paper): " %player1)
    choice2=input("%s, what s your choice (R for rock, S for Scissors and P for paper): " %player2)
    print("and the winner is...")
    time.sleep(1)
    if choice1.lower()=="r" and choice2.lower()=="s":
      print("the winner is %s" %player1)
    elif choice1.lower()=="s" and choice2.lower()=="p":
      print("the winner is %s" %player1)
    elif choice1.lower()=="p" and choice2.lower()=="r":
      print("the winner is %s" %player1)
    else:
      print("%s" %player2)
    if input("Do you wan to play again (Y/N)?").lower()=="n":
      break
  
  print("Thanks for playing, hope to see you soon...")
  
  
#RPS()

#one player version against computer.
choices={1:"s",2:"p",3:"r"}
def RPS_Alone():
  player1=input("Player 1 name: ")
  print("Hi %s , let's play!" %player1)
  while True:
    choice1=input("%s, what s your choice (R for rock, S for Scissors and P for paper): " %player1)
    choice2=random.randint(1,3)
    print("and the winner is...")
    time.sleep(1)
    if choice1.lower()=="r" and choices[choice2]=="s":
      print("the winner is %s" %player1)
    elif choice1.lower()=="s" and choices[choice2]=="p":
      print("the winner is %s" %player1)
    elif choice1.lower()=="p" and choices[choice2]=="r":
      print("the winner is %s" %player1)
    else:
      print("artificial intelligence")
    if input("Do you wan to play again (Y/N)?").lower()=="n":
      break
  
  print("Thanks for playing, hope to see you soon...")
  
RPS_Alone()
