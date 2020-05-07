# logical operators
# and or not

name = " "

# Falsy in python 0, "",  None, []

# "" -> False -(not)-> True
# .strip() to handle whitespaces
if not name.strip(): 
    print("string empty")
    
age = 22
if age >= 18 and age < 65:
    print("Eligible")
    
# we can use chaining comparison operators
if  18 <= age < 65:
    print("Eligible")