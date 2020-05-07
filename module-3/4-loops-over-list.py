letters = ["a", "b", "c"]

for letter in letters:
    print(letter)
    
for letter_touple in enumerate(letters): # introducing enumerable object
    print(letter_touple)

for index, letter in enumerate(letters): # touple unpacking similar to list unpacking
    print(index, letter)