#local variebles does not have block scope

def greet():
    if True:
        message = "a"
    print(message)
    
    
greet()