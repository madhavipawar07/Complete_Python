x = 10 #global keyword

def my_fun():
    y=5 #local keyword

    print(y)
my_fun()
print(x)

#The global keyword
x= 10 

def fun():
    global x #global keyword
    x = 3
    y = 8
    print(y)

fun()
print(x)