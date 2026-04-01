with open ('file.txt','r') as f:
    f.seek(10)
    data = f.read(5)
    print(data)
    

# tell()
with open('file.txt','r') as f:
    data = f.read(5)
    print(data)

    cur_pos = f.tell()
    f.seek(cur_pos)

# truncate()
with open('file1.txt','w') as f:
    f.write("Hello World!")
    f.truncate(4)

with open('file1.txt','r') as f:
    print(f.read())

#tell
with open("file2.txt", "r") as f:
    print(f.tell())   # position at start

    f.read(5)
    print(f.tell())   # position after reading 5 characters