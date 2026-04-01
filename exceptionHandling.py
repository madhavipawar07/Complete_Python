try:
    a = int(input("Enter a number: "))
    print(f"Multiplication table of {a} is:")

    for i in range(1, 11):
        print(f"{a} x {i} = {a*i}")

except :
    print("Invalid input! Please enter a valid number.")

print("Some imp lines of code")
print("End of program")


try:
    num = int(input("Enter an integer: "))
    a = [6, 4]
    print(a[num])

except ValueError:
    print("Index Error")