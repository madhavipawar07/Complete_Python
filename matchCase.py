x = int( input("Enter the value of x : "))
match x: 

    case 0:
        print("x is zero")

    case 4:
        print("x is four")

    case _ if x!=90:
        print(x, "is not 90")

    case _ if x!= 50:
        print(x, "is not 50")

    case _:
        print(x)

day = 8

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case _:
        print("Invalid day")


choice = int(input("Enter your choice (1–3): "))

match choice:
    case 1:
        print("You selected Tea")
    case 2:
        print("You selected Coffee")
    case 3:
        print("You selected Juice")
    case _:
        print("Invalid choice")