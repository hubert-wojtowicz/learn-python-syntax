from sys import getsizeof

size = 10
print("list...")
list_odd_numbers = [x * 2 + 1 for x in range(size)]
print(type(list_odd_numbers))
print(list_odd_numbers)

print("generator...")
generator_odd_numbers = (x * 2 + 1 for x in range(size))
print(type(generator_odd_numbers))
print(generator_odd_numbers)
print(list(generator_odd_numbers))

list_odd_numbers_big = [x * 2 + 1 for x in range(size ** 3)]
print("list_odd_numbers_big size: ", getsizeof(list_odd_numbers_big))

generator_odd_numbers_big = (x * 2 + 1 for x in range(size ** 3))
print("generator_odd_numbers_big size: ", getsizeof(generator_odd_numbers_big))