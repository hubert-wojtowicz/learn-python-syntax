numbers = [4, 51, 2, 8, 6]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

print(sorted(numbers))

item = [
    ("Product1", 10),
    ("Product2", 3),
    ("Product3", 12),
]

item.sort()
print(item) # does not kno comparator


def sort_item(item):
    return item[1]
    
item.sort(key=sort_item)
print(item) # does not kno comparator
