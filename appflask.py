

from flask import Flask

app = Flask(__name__)

#Home page
@app.route("/")
def home():
    return "<h1>📚 Library Book Tracker</h1>"

#About page
@app.route("/about")
def about():
    return """
    <h1>About Us</h1>
    <p>This app helps you keep track of your library books.</p>
    <a href="/">back to Home</a>
    """
#Books page
@app.route("/books")
def books():
    
    books = [
        {"book_id": 1,
         "title": "The Great Gatsby",
         "author": "F. Scott Fitzgerald",
         "available": True},
        {"book_id": 2,
         "title": "To Kill a Mockingbird",
         "author": "Harper Lee",
         "available": False},
        {"book_id": 3,
         "title": "1984",
         "author": "George Orwell",
         "available": True},
         {"book_id": 4,
            "title": "Pride and Prejudice",
            "author": "Jane Austen",
            "available": False }
    ]

    html = "<h1>Books in Library</h1><ul>"

    for b in books:
        status = "Available" if b["available"] else "Issued"
        html += f"<li>{b['title']} by {b['author']} - {status}</li>"

    html += """
    </ul>

    <form>
        <input type="text" name="title" placeholder="Book Title" required>
        <input type="text" name="author" placeholder="Author Name" required>
        <button type="submit">Add Book</button>
    </form>

    <br>
    <a href="/">Back to Home</a>
    """
    return html

print("Starting Flask app...")
print("--name--")

if __name__ == "__main__":
    app.run(debug=True)