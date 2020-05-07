item = [
    ("Product1", 10),
    ("Product2", 3),
    ("Product3", 12),
]

x = list(filter(lambda item:item[1] >= 10, item))
print(x)