letters = ["a", "b", "c",  "d"]
print(letters)
print(letters[0])
print(letters[-1])
print(letters[-3])
print(letters[1:3]) # slice
print(letters[:]) # get copy of string in memory
print(letters[::2]) # 2 is step size

numbers  = list(range(20))
print(numbers[::2])
print(numbers[::-1]) # reverse order