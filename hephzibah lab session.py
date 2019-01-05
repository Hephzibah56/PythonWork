a=3
b=2
c=a+b
print(c)

x=10
y=2
z=x+y
print(z)

def sum(a,b):
        sum=(a+b)
        return sum
B=sum(2,3)
print(B)

def sum(x,y):
    sum=(x+y)
    return sum
C=sum(10,54)
print(C)

def area(L,B):       
    area=(L*B)       
    return area      
X=area(10,2)        
print(X)            

def perim(L,B):
    perim=((2*L) + (2*B))
    return perim
result=perim(3,8)
print(result)

def perimeter(l,b):
    perimeter=(l*b)
    return perimeter
length=int(input("input length"))
Length=3
breadth=int(input("input breadth"))
breadth=5
print()

#genericfunction
def genericfunction(X,Y,operator):
    if operator==("sum"):
        return sum(X,Y)
    elif operator=="area":
        return area (X,Y)
    elif operator=="perimeter":
        return perimeter(X,Y)
    else:
        return ("invalid operator")
operator=input("enter the operation you want to perform e.g sum, area, perimeter")
operator=sum
first number = int(input("enter the firstnum"))
first number=5
second num=int(input("enter the secondnum"))
second number=6
ans=generic function(firstnum,secondnum, operator)
print(ans)
