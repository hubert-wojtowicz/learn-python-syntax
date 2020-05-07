stack = [1, 2, 3]
stack.append(4)

print(stack) 
print(stack.pop())
print(stack) 

while stack:
    print("Poping...")
    print(stack.pop())