#!/usr/bin/env python3

# CHALLENGE:
'''
Given an integer,

perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of to print Not Weird
If n is even and in the inclusive range of to print Weird
If n is even and greater than print Not Weird

Input Format:
A single line containing a positive integer.
'''

# ANSWER:
n = int(input())

if n < 1 or n > 100:
    print()
elif n % 2 != 0:
    print('Weird') 
elif n % 2 == 0 and n <= 5:
    print('Not Weird')
elif n % 2 == 0 and n >=  6 and n <= 20:
    print('Weird')
elif n % 2 == 0 and n > 20:
    print('Not Weird')
