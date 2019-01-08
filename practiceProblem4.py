"""Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre.
"""
X = float(input(" Enter the width of the field:"))
Y = float(input (" Enter the length of the field:"))
# 43,560 square feet represent 1 acre
H = (X*Y)/(float(43560))
print( str(H) + " acres")
