numbers = [1, 2, 3]
# first = numbers[0]
# second = numbers[1]
# thirt = numbers[2]

first, second, third = numbers # list unpacking - numbers of elements must fit

_numbers = list(range(10))
_first, *_other = _numbers # workaround for number of elements

print(_first)
print(_other)

__first, *__other, __last = _numbers

print(__last)