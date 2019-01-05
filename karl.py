def testIsogram(x):
    x = x.lower()
    print(x)
    for i in range(0,len(x)):
        if x.count(x[i]) != 1:
            return False
    return True
value = input('Enter the string: ')
if testIsogram(value):
    print(value + " is an isogram")
else:
    print(value + " is not an isogram")