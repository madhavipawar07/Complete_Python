name = "Harry"
anotherName = 'Alice'
apple = '''He said,
Hi Alice 
hey I am good 
I want to eat an apple'''
print(name)
print(anotherName)
print (apple)

print(name[0])
print(name[3])

#using for loop

for char in name:
    print(char)

    for char in apple:
        print(char)

#String Slicing 

names= "Madhavi"
print(len(names))

fruit = "Mango" 
len1=len(fruit)
print("Mango is a",len1 ,"letters word")
print(fruit[0:])
print(fruit[1:4])
print(fruit[:])
print(fruit[-3:-1]) #length-given value
print(fruit[-3:2])
nm="Harry"
print(nm[-4:-2])

#String methods

str = "Hello***"
#rstrip ()
print(str.rstrip("*"))


#replace()
print(str.replace("Hello", "welcome"))


#split()
str1 = "welcome to the python series"
print(str1.split(" "))

#capitalize()
print(str1.capitalize())
str2 = "hello WorlD"
print(str2.capitalize())

#center()
print(str1.center(100))
print(len(str1))
print(len(str1.center(100)))

#count()
print(str1.count("t"))
print(str1.count("th"))

#endswith()
print(str2.endswith("t"))
print(str2.endswith("orlD"))
print(str2.endswith("Wor",6,9))

#find()
str3 = "Python is widely used language"
print(str3.find("used"))
print(str3.find("job"))


#index()
print(str3.index("thon"))

#isalnum()
str4 ="madhavi8"
print(str4.isalnum())

#isalpha()
print(str4.isalpha())

#islower()
print(str4.islower())

#isprintable()
print(str4.isprintable())

#isspace()
s="     "
print(s.isspace())
print(str3.isspace())

#istitle()
s1 = "Python Series"
print(s1.istitle())


#isupper()
s2 = "ALICE"
print(s2.isupper())


#startswith()
print(str3.startswith("P"))

#swapcase()
print(s2.swapcase())
print(str3.swapcase())

#title()
print(str3.title())






