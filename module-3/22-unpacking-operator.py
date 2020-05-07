numbers = [1, 2, 3]
print(numbers)
print(*numbers)

values = list(range(5))
print(values)
print(*values)

first = [1, 2]
second = [3, 4]
print([*first, *"abc", *second])

## for dictionaries use **
dict1 = dict(x=1)
dict2 = dict(x=2,y=3)
combined = {**dict1, **dict2, "z": 1} # for the same key the very last value used
print(combined)