class Student:
    def __init__(self):
        self

    def returnBook(self):
        self.book = input("Enter the book name you want to return\n")
        return self.book

    def requestBook(self):
        self.book = input("Enter the book name you want to borrow\n")
        return self.book


class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books Present in library are:")
        for index, Books in enumerate(self.books):
            print(index, Books)

    def borrowBook(self, BookName):
        if BookName in self.books:
            print("Yes Book is available,Now the books has been issued on your name")
            self.books.remove(BookName)
        else:
            print("Sorry,This Book has been already issued")
    def ReturnBook(self,BookName):
        print("Thank you! for returning the book on time")
        self.books.append(BookName)

if __name__ == "__main__":
    centralLibrary = Library(
        ["Python", "Django", "Data Structure", "Algorithms", "Ajava", "Discrete Mathematics"])
    #centralLibrary.displayAvailableBooks()
    student = Student()
    while(True):
        welcomeMsg = ''' ____Welcome to the central Library____
        Please Choose the one below option
        1 Listing all the Books
        2 Add/Return a Book
        3 Request a Book
        4 Exit the Library
        '''
        print(str(welcomeMsg))
        a = int(input("Enter  your choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.ReturnBook(student.returnBook())
        elif a==3:
            centralLibrary.borrowBook(student.requestBook())
        elif a==4:
            print("Thank you for coming ,Have  a Great Day!")
            exit()
        else:
            print("please enter valid option")
