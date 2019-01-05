def is_square(n):
    import math
    if n < 0:
        print(str(n) + ": Negative numbers cannot be square numbers")
        return False
    elif n > 0:
        x = math.sqrt(n)
        if x == int(x):
            print(str(n) + " is a square number")
            return True
        else:
            print(str(n) + " is not a square number")
            return False
    else: 
        print("0 is a square number")
        return True
    