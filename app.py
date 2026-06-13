from flask import Flask, render_template, request
from practice import get_db

app = Flask(__name__)

# Books chi list - hich use karaychi
books = [
    {"title": "Python Programming", "author": "Guido Van Rossum", "price": 500},
    {"title": "Flask Web Development", "author": "Miguel Grinberg", "price": 450},
    {"title": "Data Science Handbook", "author": "Jake VanderPlas", "price": 600},
    {"title": "Machine Learning Yearning", "author": "Andrew Ng", "price": 750}
]

# Database Table banavnyasathi function
def create_table():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll TEXT,
            marks INTEGER,
            subject TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Server chalu kelya kelya table banav
create_table()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/books")
def books_page():
    return render_template("books.html", books=books)

@app.route("/search")
def search():
    q = request.args.get('q', '')
    conn = get_db()
    if q:
        students = conn.execute(
            "SELECT * FROM students WHERE name LIKE ? OR subject LIKE ? OR roll LIKE ?", 
            (f'%{q}%', f'%{q}%', f'%{q}%')
        ).fetchall()
    else:
        students = conn.execute("SELECT * FROM students ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("search.html", students=students, q=q)

@app.route("/add-sample")
def add_sample():
    conn = get_db()
    conn.execute("INSERT INTO students (name, roll, marks, subject) VALUES (?, ?, ?, ?)",
                 ("Shlok", "101", 95, "Math"))
    conn.execute("INSERT INTO students (name, roll, marks, subject) VALUES (?, ?, ?, ?)",
                 ("Tanuja", "102", 88, "Science"))
    conn.commit()
    conn.close()
    return "2 Students Added! Ata /search var ja"

if __name__ == "__main__":
    app.run(debug=True)