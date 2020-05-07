message = "a"

def greet():
    #global message # uncomment if want to use global message varieble inside this function (bad practice)
    message = "b"

print(message)
greet()
print(message)