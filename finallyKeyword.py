def func():
    try:
        l = [1,2,5,7,8]
        i = int(input("Enter the index:"))
        print(l[i])
        return 1
    
    except:
        print("Some error occurred")
        return 0
    
    finally:
        print("I am always executed")


x = func()
print(x)



    