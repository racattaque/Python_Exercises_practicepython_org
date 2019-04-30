# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html:

# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

def evenOdd():
  number=int(input("Please provide a number: "))
  if number%2==0:
    print("The number %d is even !" %number)
  else:
    print("The number %d is odd !" %number)
  if number%4==0:
    print("In addition, it is divisible by 4!")
  else:
    print("But it is not divisible by 4")
  num=int(input("Let s push it further, give me a number: "))
  check=int(input("Do you doubt if it is divisible by something? Tell me what to check and I will check that for you: "))
  if num%check==0:
    print("Yes, %d is divisible by %d" %(num, check))
  else:
    print("Unfortunately not, %d is not divisible by %d" %(num, check))
  
  
evenOdd()