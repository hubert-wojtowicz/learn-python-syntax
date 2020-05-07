item = [
    ("Product1", 10),
    ("Product2", 3),
    ("Product3", 12),
]

item.sort(key=lambda item:item[1])
print(item) # does not kno comparator