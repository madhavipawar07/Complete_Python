# for i in range (1,101,1):
#     print(i, end =" ")
#     if( i==50):
#         break
#     else:
#         print("Python")
# print("Thank you")


# for i in range(12):
#     if( i==10):
#         break

#     print("5 X", i, "=", 5*i)


 #continue

for i in [2,3,4,6,8,0]:
    if(i % 2 !=0):
        continue
    print(i)


for i in range(12):
    if ( i==10):
        print("Skip the iteration")
        continue

    print("5 X",i, '=',5 *i)