"""
In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.
"""
x= float(input(" Enter the numbers of liters of fuel bought in America(MPG): "))
y = ("%.3f"% (x/100))
print(y + " the number of liters in (L/100 km).")
