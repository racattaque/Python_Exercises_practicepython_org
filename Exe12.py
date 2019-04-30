__author__="racattaque"
# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.


def trunkList(list):
 #Can also use 'len(list)-1' to get the last element instead of '-1'
 return [list[0],list[-1]]

print(trunkList([5, 10, 15, 20, 25]))