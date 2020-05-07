def fizz_buzz(input: int) -> str:
    FizzBuzz = ""
    if input % 3 == 0: 
        FizzBuzz += "Fizz"
    if input % 5 == 0:
        FizzBuzz += "Buzz"
    
    if FizzBuzz:
       return FizzBuzz
    else:
        return input
        
print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(7))
print(fizz_buzz(21))