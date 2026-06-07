 # library book tracker 
books = []
def issue_book():
    book_name =input("Enter book name:")
    student_name = input("Enter student name:")
    issue_date = input("Enter issue date (YYYY-MM-DD):")
    due_date = input("Enter due date (YYYY-MM-DD):")
    books.append([book_name, student_name, issue_date, due_date])
    print ("Book issued successfully!")
def return_book():
    book_name = input("Enter book name to return:")
    for book in books:
        if book[0] == book_name:
            books.remove(book)
            print("Book returned successfully!")
            return
    print("Book not found!")
def display_books():
    if not books:
        print("No books issued.")
    else:
        print("Issued Books:")
        for book in books:
            print(f"Book: {book[0]}, Student: {book[1]}, Issue Date: {book[2]}, Due Date: {book[3]}")
while True:
    print("\nLibrary Book Tracker")
    print("1. Issue Book")
    print("2. Return Book")
    print("3. Display Issued Books")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        issue_book()
    elif choice == '2':
        return_book()
    elif choice == '3':
        display_books()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")