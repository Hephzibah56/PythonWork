"""
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
  The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of ab
"""
import math
h = int(input(" Enter the value of A: "))
y = int(input(" Enter the value B: "))
# the sum of a and b
m = (h+y)
# the difference of a-b
x = (h-y)
#the product of a and b
k = (h*y)
# part 2 of the question
# the quotient of a and b
p = (h/y)
# the remainder/modulus when a divided by b
q = (h%y)
#logarithms of log10^a
n = math.log10(h)
w = (str(h) + str(y))
print(str(m) + " is the additon of your numbers" + "\n" + str(x) + " is the difference of your numbers" + "\n" + str(k) +" is the product of your numebrs")
print(str(p) + " is the quotient of the numbers" + "\n" + str(q) + " is the modulus of your numbers" + "\n" + str(n) + " is the logarithm of numbers"  + "\n" + str(w) + " result of ab")
