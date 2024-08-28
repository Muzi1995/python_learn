users = ['Dave', 'John', 'Sara']

data = ['John', 42, True]

emptylist = []

print('John' in emptylist)

# Printing users by their positions including - values as well.

print(users[0])
print(users[-1])
print(users[-2])

# Finding the position of a specific value

print(users.index('John'))

# Finding range of values (by positions)

print(users[0:2])

# Finding everything from first to the last position - We would not provide an ending value

print(users[1:])

# It can return Negative Numbers as well

print(users[-3:-1])

# Returning the Length of our list

print(len(data))

# Adding more items to an existing list. Adding Elsa to users list:

users.append('Elsa')
print(users)

# Adding new list to our previously existing list: Two lists both named users
# Point to note if we had only typed += 'Jason' it could consider each letter as
# a seperate value.

users += ['Jason']
print(users)

# Adding new list to a previously existing list using the 'Extend Method'

users.extend(['Robert', 'Jimmy'])
print(users)

# Adding a list to previously existing list: (Commenting becuase don't need a list with random items)

# users.extend(data)
# print(users)

# All the previous additions to lists are at the end
# Now we pick the positions in the list using the INSERT method.

users.insert(0, 'Bob')
print(users)

# We can also add users by brackets. Here we are adding two values in the middle.
# This is why range is defined here as well as [2:2]

users[2:2] = ['Eddie', 'Alex']
print(users)

# Replacing the values. We used 3 becuase it stops at the third position
# it does not replace what is at the thrid position

users[1:3] = ['Robert', 'JPJ']
print(users)

# Removing data (values) from a list

users.remove('Bob')
print(users)

# Popping the last item in the list using the POP method. The last item in the
# list gets popped off.

print(users.pop())
print(users)

# Deleting a specific user from the list. Robert gets removed. At 0 index.

del users[0]
print(users)

# Deleting a list completely:

# del data
print(data)

# Clearing the list but it still exists

data.clear()
print(data)

# Sorting the list
# When sorted dave comes last due to case-sensitivity
# when we passed the key=str.lower then it is sorted in the list with alphabetical position
# Also it worked on the same type of data: Remember.

users[1:2] = ['dave']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

# Numbers Lists
# Reversing the list: Not sorting. Reversing the order of elements in the list.

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))

# Making copies of original lists:

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

# Checking the type of list:

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

# Tuples

mytuple = tuple(('Dave', 42, True))

# assignging values to tuple called packing a tuple
anothertuple = (1, 4, 2, 8, 2, 2)
print(mytuple)
print(type(mytuple))
print(type(anothertuple))

# Since Tuples cannot be changed. We can create copies as list and then make amends:

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

# Unpacking a tuple

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

# This shows how many countings of 2 are in the tuple

print(anothertuple.count(2))
