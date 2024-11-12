# FizzBuzz game: prints numbers from 1 to 100 with the following rules:
# - Print "Fizz" for numbers divisible by 3
# - Print "Buzz" for numbers divisible by 5
# - Print "FizzBuzz" for numbers divisible by both 3 and 5
# - answer for this challenge from the 40 th line !! but try once



































for number in range(1, 101):
    if number % 3 == 0 and (number % 5 == 0):
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif (number % 3 == 0):
        print("Fizz")
    else:
        print(number)
