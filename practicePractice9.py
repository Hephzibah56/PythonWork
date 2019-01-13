"""
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places
"""
x= float(input("Enter the current amount of money you have in your account: "))
# amount in the first year
y = float((x*0.04) + x)
# amount in the second year
z = float((y*0.04) + y)
# amount in the third year
m =float((z*0.04) + z)
print(str(y + z + m) + " is the total money you have in your bank account")
