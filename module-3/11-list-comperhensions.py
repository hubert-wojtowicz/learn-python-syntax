items = [
    ("Product1", 10),
    ("Product2", 3),
    ("Product3", 12),
]
# [expression for item in items]
# prices = list(map(lambda item:item[1], item))

prices = [item[1] for item in items]
print(prices)

# filter = list(filter(lambda item:item[1] >= 10, item))
filter = [item for item in items if item[1] >= 10]
print(filter)
