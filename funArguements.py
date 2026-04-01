#Required Arguements
def avg(a, b=9):
    print("The average is =", (a+b)/2)

avg(8)

#////////////////////////

#Default Arguements
def average(c=4, d=8):
    print("The average is=",(c+d)/2)

average(d=2)

#//////////////////////////

#Keyword Arguements
def name(fname,lname,mname):
    print("Hello",fname,mname,lname)

name(mname="Peter", lname="Watson", fname="Alice")

#//////////////////////


#keyword Arbitrary Arguments
def name(**name):
    print(type(name))
    print("Hello",name["fname"],name["mname"],name["lname"])

name(mname="Peter", lname="Watson", fname="Alice")


def avg(*numbers):
    sum=0
    for i in numbers:
        sum = sum +i
    return sum/len(numbers)
    #print("The average is :",sum/len(numbers))

avg(8,2,6)