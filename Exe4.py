# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

number=int(input("What is the number you want to get all the divisors?\n"))
a=[]
for i in range(1,number+1):
  if number%i==0:
    print("%d is a divisor of %d" %(i, number))
    a.append(i)
print("\n")
print("To recapitulate, all the divisors are:\n")
print(a)

print("\n")
print("Second method")
#comprehensive lists
print([a for a in range(1,number+1) if number%a==0])