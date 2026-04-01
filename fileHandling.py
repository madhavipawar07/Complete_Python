#reading from file

f = open('file.txt', 'r')
contents = f.read()
print(contents)
f.close()

#writing to file

f = open('file.txt','w')
f.write("It is a python programming")
f.close()


# with statement
with open('file.txt','a') as f:
    f.write("Hey I am inside with") 