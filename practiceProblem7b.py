"""Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
"""
import time
y = time.time()
n= int(input("Enter the numbers that are positive integers: " ))
sum = 0
sum = ((n*(n+2))/2)
z = time.time()
print(sum)
print("This program started at " + str(y) + " and ends at " + str(z))
