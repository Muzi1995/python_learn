from functools import reduce

# lambda num: num * num


def squared(num): return num * num


print(squared(2))


# lambda num: num + 2

def addTwo(num): return num + 2


print(addTwo(12))

# lambda a, b: a + b


def sum_total(a, b): return a + b


print(sum_total(10, 8))

# add = lambda x, y: x + y


def add(x, y): return x + y


result = add(5, 3)
print(result)


############################################


def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))


############################################
# High Order Functions

lambda num: num * num
numbers = [3, 7, 11, 18, 20, 19]

square_nums = map(lambda num: num * num, numbers)
print(list(square_nums))

############################################

lambda num: num % 2 != 0
odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_nums))


numbers = [2, 5, 67, 89, 12, 24, 8, 9]

total = reduce(lambda acc, curr: acc + curr, numbers)

print(total)

print(sum(numbers))

#############################################

lambda acc, curr: acc + len(curr)
names = ["Muzi Kim", "Adam goes to zoo", "King", "Chris"]
char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count)
