a = int (input("Enter the number between 5 and 9"))

if a<5 or a>9:
    raise ValueError("The number should be between 5 and 9")


i = input("Enter the word =")

if i != "quit":
    raise ValueError("The word entered should be quit ") 