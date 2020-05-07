def increment(number: int, by: int=1) -> tuple:
    return (number, number + by)

print(increment(2))
print(increment(2, 10))
print(type(increment(2, 3)))