"""Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
"""
import time
n = int(input("Enter a number that is a positive integer: "))
sum = 0
x = time.time()
for i in range(1,n+1):
    sum += i
print(sum) # it is printing the value of sum
y = time.time()
print("This program started at " + str(x) + " and ends at " + str(y))
