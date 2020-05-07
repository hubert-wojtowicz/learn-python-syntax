letters = ["a", "b", "c", "d", "e"]

print(letters.index("b"))
if "x" in letters:
    print(letters.index("x")) # if this "x" doesn't exist it will stop program with ValueError

print(letters.count("e"))
print(letters.count("x"))