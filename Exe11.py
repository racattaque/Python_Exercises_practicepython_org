__author__='racattaque'

# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

#imported to use the exit function 


print("Welcome to check prime numbers function")

#create a function that checks if a number is prime or not. returns True or False
def isPrime(toCheck):
  for num in range(2,toCheck):
    if toCheck%num==0:
      return False
  return True

while True:
  toCheck=input("What is the number you want to check (or q to quit)? ")
  if toCheck.lower()=='q':
    break
  else:
#To manage exceptions, if int fail to convert the user input to integer (String input), then it will execute the except block.
    try:
      toCheck=int(toCheck)
    except:
      print("Prime notion is defined for numbers only, you may try to give your definition for other stuffs :)")
      continue
    if isPrime(toCheck):
      print("Yes, %d is a prime number" %toCheck)
    else:
      print("%d is not a prime number" %toCheck)