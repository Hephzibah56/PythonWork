#genericfunction
def sum(x,y):
    return x+y

def area(L,B):
    area=(L*B)
    return area

def perim(L,B):
    perim=((2*L) + (2*B))
    return perim


def genericfunction(X,Y,operator):
    if operator=="sum":
        return sum(X,Y)
    elif operator=="area":
        return area(X,Y)
    elif operator=="perimeter":
        return perimeter(X,Y)
    else:
        return ("invalid operator")

operator=input( "enter the operation you want to perform e.g sum, area, perimeter")
firstnum=int(input("enter the firstnum"))
secondnum=int(input("enter the firstnum"))
ans=genericfunction(firstnum,secondnum,operator)
print(ans)

