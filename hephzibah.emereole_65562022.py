    # STAGES OF  LIFE OF A USER


print("Enter age group"+"\n")
age=input("Input Age group: ")
age = int(age)

if age >= 0 and age < 1:
    print("you are a baby")
elif age>= 1 and age<= 2:
    print("you are a toddler")
elif age>= 3 and age<= 6:
    print("you are qualified to be in pre-school")
elif age>= 7 and age<= 12:
    print("you are qualified to be in Grade-school")
elif age>= 13 and age<= 18:
    print("you are a teenager")
elif age>= 19 and age<= 25:
    print("you are a young adult")
elif age>= 26 and age<= 39:
    print("you are a young adult")
elif age>= 40 and age<=60:
    print("you are a middle aged Adult")
elif age>= 61:
    print("you are aged")
#incase of a negative age
else:
    print("invalid age")
    
