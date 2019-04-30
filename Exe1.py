# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html:
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)


import datetime

def age_100():
 name=input("Hi, what is your name?\n")
 age=int(input("Nice to meet you %s. How old are you?\n" %(name)))
 now = datetime.datetime.now()
 year=now.year
 msg="You know %s, you will turn 100 years old in %d" %(name, year - age + 99)
 print(msg)
 number=int(input("Give me a number: "))
 for i in range(0,number):
   print(msg)
 
 
age_100()