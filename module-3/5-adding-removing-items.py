letters = ["a", "b", "c", "d", "e"]

# Adding
letters.append("f")
print(letters)

letters.insert(0, "-")
print(letters)

# Removing
letters.pop()
print(letters)

letters.pop(0)
print(letters)

letters.remove("b")
print(letters)

del letters[1:3]
print(letters)

letters.clear()
print(letters)