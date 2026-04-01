class Library:
    def __init__(self):
        self.nobooks = 0
        self.books = []

    def addbook(self, book):
        self.books.append(book)
        self.nobooks = len(self.books)

    def showInfo(self):
        print(f"The library has {self. nobooks} books. The books are")
        for book in self.books:
            print(book)

l1 = Library()
l1.addbook("Harry POtter1")
l1.addbook("Harry POtter2")
l1.addbook("Harry POtter3")
l1.addbook("Harry POtter4")
l1.addbook("Harry POtter5")
l1.showInfo()