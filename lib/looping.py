#!/usr/bin/env python3

def happy_new_year():
    # Countdown from 10 to 1 and then print "Happy New Year!"
    number = 10
    while number > 0:
        print(number)
        number -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # Return a list of squared integers from the input list
    return [x**2 for x in int_list]

def fizzbuzz():
    # Print numbers from 1 to 100 with conditions for Fizz, Buzz, and FizzBuzz
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
