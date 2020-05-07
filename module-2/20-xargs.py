def multiply(*list):
    print(list)
    print(type(list))
    total = 1
    for number in list:
        total *= number
    return total
    
print(multiply(1,2,3,4,5))