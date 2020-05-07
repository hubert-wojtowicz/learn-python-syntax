numbers = [1, 1, 2, 3, 4]
first = set(numbers)
print(first)

second = {1, 1, 4, 7}
print(second)

print(first | second) # union
print(first & second) # intersection
print(first - second) # substraction
print(first ^ second) # symetric difference - either 1st or 2nd not in both

if 1 in first:
    print("yes")

# not supporting indexing in sets
print(first[0])

# set recap - unorder collection of unique items without access by index