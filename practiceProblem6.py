"""
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.
"""
x = float(input("Enter the cost of a meal: "))
y = float(x*0.18) # cost of meal tip
print (str(y) + " is the tip you are giving to the waitress" ) # cost of meal tip without tax
Z= 10  # income tax payment
print (str((x+y) + (x*0.1)) +" is your grand total.")
