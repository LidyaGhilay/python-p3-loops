#!/usr/bin/env python3

def happy_new_year():
    counting = 10
    while counting > 0:
        print(counting)
        counting -= 1
    print("Happy New Year!")

happy_new_year()

def square_integers(int_list):
    squared = [s**2 for s in int_list]
    return squared

int_list = [] 

def fizzbuzz():
    for i in range(1, 101):  
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizzbuzz()
