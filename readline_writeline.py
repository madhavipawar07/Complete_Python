#readline()

f = open('file.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)


#writeline()

# # f = open('myfile.txt','w')

# lines = ['line1\n','line2\n','line3\n']

# f.writelines(lines)

# f.close()

f = open('myfile.txt', 'w')
lines = ['strawberry','mango','orange','grapes']
for line in lines:
    f.writelines(line +'\n')
f.close()