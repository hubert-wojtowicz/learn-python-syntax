# more preformant, less memory
# for large sequences
# 10k or more

from array import array

numbers = array("i", [1, 3, 4])

numbers.append(5)
numbers.insert(2, 1)
print(numbers)

#causing error
numbers[0] = 1.0