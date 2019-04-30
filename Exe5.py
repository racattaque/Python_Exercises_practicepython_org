# Take two lists, say for example these two:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print([x for x in a for y in b if (x not in x) and (x==y)])

list=[]
for itemA in a:
  for itemB in b:
    if itemA==itemB:
      if itemA not in list:
        list.append(itemA)
print(list)


#Second method in one line by @haseem
a = [1,1,1,6,7,8,9,4,9]
b = [1,6,87,98,67,45,10,11,12,13,14,15,16]
print(set(a) & set(b))