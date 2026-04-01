# def factorial(n):
#     if n == 0:
#         return 0
#     elif n== 1:
#         return 1
#     else:
#         return (n * factorial(n-1))
    
# no = int(input("Enter the number : "))
# print("The factorial of a number is :",factorial(no))

#Fibonacci Series
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

terms = int (input("Enter the no:"))
print("Fibonacci Series")

for i in range(terms):
    print(fibonacci(i), end =" ")