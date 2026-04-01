def calculateGmean (a,b):
    mean = ( a*b) / (a+b)
    print(mean)

def isGreater(a, b):
    if( a > b):
        print("First no is greater")

    else:
        print("Second no is greater")

def isLesser (a,b):   
    pass                  #reserved to use later

a= 8
b= 6

calculateGmean(a,b)
isGreater(a,b)

c=4
d=10

calculateGmean(c,d)
isGreater(c,d)