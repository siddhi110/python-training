 # Main Entity Dictonary(library book tracker)
books =[
    {
        "book_id": 101,
        "title": "Python Basics",
        "author": "John smith",
        "status":"Issued",
        "due_days": 5
    },
    {
        "book_id": 102,
        "title": "Data Structures",
        "author": "Robert Brown",
        "status": "Available",
        "due_days": 0
    },
    {
        "book_id": 103,
        "title": "Machine Learning ",
        "author":"Andrew Ng",
        "status":"Issued",
        "due_days": 2
    },
    {
        "book_id":104,
        "title": "Web Development",
        "author": "David Miller",
        "status":"Available",
        "due_days": 0
    },
    {
        "book_id": 105,
        "title": "Database Systems",
        "author":"James Lee",
        "status":"Issued",
        "due_days":10
    }
]

library_info =[
    {
    "library_name":"Goverment Polytechnic Library",
    "location":"Hingoli",
    "total_books":5000,
    "librarian":"Mrs.patil",
    "established_year": 2000
    }
]

def get_status(status):
    if status =="Available":
        return "Ready to Issue"
    else:
        return "Currently Barrowed"
    

def calculate_fine(days):
    if days >7:
        return(days-7)* 5
    return 0

def search_book():
    title = input("Enter Book Title: ")
    
    for book in books:
        if book ["title"].lower() ==title.lower():
              
         print("\nBook Found!")
         print("Book ID :",book["book_id"])
         print("Title :",book["title"])
         print("Author :",book["author"])
         print("Status :",book["status"])
         print("Due Days :",book["due_days"])
         print("Fine :Rs.",book["due_days"])
         return
        
        print("Book Not Found")

print("\n---Library Books---")

for book in books:
    print("\nTitle:",book["title"])
    print("Author:",book["author"])
    print("Status:",get_status(book["status"]))


search_book()