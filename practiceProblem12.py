"""
The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
surface. The distance between these points, following the surface of the Earth, in
kilometers is:
distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))
The value 6371.01 in the previous equation wasn’t selected at random. It is
the average radius of the Earth in kilometers.
Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers.
Method 2: values = input("Enter the values: "). split()
for k in values:
    k = int(k)
z = float( 6371.01 * arccos(sin(values[0]) * sin(values[1]) + cos(values[0]) * cos(y) * cos())
z = float( 6371.01 * arccos(sin(h) * sin(y) + cos(h) * cos(y) * cos())
"""
import math
h = int(input("Enter the first latitude of your city (in degrees): ")) #t1
y = int(input(" Enter the first longitude of your city (in degrees): ")) #t2
z = int(input("Enter the second latitude of your city (in degrees): "))#g1
j = int(input(" Enter the second longitude of your city (in degrees): "))#g2
z = float( 6371.01 * (math.acos(math.sin(h) * math.sin(y) + math.cos(h) * math.cos(y) * math.cos( z- j))))
print( str(z) + " distance between two points in kilometers")
