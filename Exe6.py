__author__ = 'racattaque'

# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

inputStr=input("Give you word, let s check if it is a palindrome or not:\n").strip()
i = 0
while i < len(inputStr) and inputStr[len(inputStr)-1-i].lower()==inputStr[i].lower():
  i+=1
if i ==len(inputStr): 
  print("Your word is a palindrome")
else:
  print("It is not a palindrome")

