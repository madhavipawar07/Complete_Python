import pandas as pd

dic = {"a":[1,2,3,4,5],"b":[0,6,7,8,9],"c":[11,12,13,14,15]}

d = pd.DataFrame(dic)
print(d)

#index = False removes the index
d.to_csv("Test_new.csv",index=False)

#Header changes the index value
d.to_csv("Test_new1.csv",index = False,header=[1,2,3])

data={"id":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],"name":["Madhavi","Gaurav","Aditya","Varad","Khushi","Akshada","Harshada","Raj","Mihir","Siddhesh","Priyanshu","Hemal","Ritesh","Anuja","Priyanka"],"marks":[89,87,87,79,86,78,87,84,85,80,82,78,80,81,80],"age":[21,21,21,21,20,20,21,21,20,21,20,21,20,20,21]}

d1=pd.DataFrame(data)
print(d1)

d1.to_csv("Students.csv",index=False)