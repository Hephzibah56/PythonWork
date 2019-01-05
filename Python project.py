
import random

#pick a random number
print("to exit enter -1")
unknown_number = random.randint(1,150)
guess= int(input("input number between 0 and 150 "))
if guess >= 150: 
            print("your number should not exceed 150")
                
while unknown_number!=guess and guess!=-1:
    if guess>unknown_number:
       guess=int(input("choose a lesser number: "))
       if guess >= 150: 
            print("your number should not exceed 150")
            break
    
    elif guess< unknown_number:
        guess=int(input("choose a larger number: "))
        if guess >= 150: 
            print("your number should not exceed 150")
            break
    if guess==unknown_number :
       print(" CONGRATS! You got it")
       
        


    