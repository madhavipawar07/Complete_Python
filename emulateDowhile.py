i= 0

while True:
    print(i)
    i=i+1
    if(i % 100 ==0):
        break

 #2nd example
while True:
    number = int(input("Enter the number ="))
    print(number)
    if not number <= 0:
        print("Loop is stopping now")
        break
print("Outside the loop")