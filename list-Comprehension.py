first = [i*i for i in range (10)]
print(first)

first = [i*i for i in range (10) if i%2==0]
print(first)


result = ["Even" if i % 2 == 0 else "Odd" for i in range(5)]
print(result)


names = ["madhavi", "python", "code"]
upper_names = [name.upper() for name in names]
print(upper_names)