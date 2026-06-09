from flask import Flask, render_template

app = Flask(__name__)

# Books chi list - hich use karaychi
books = [
    {"title": "Python Programming", "author": "Guido Van Rossum", "price": 500},
    {"title": "Flask Web Development", "author": "Miguel Grinberg", "price": 450},
    {"title": "Data Science Handbook", "author": "Jake VanderPlas", "price": 600},
    {"title": "Machine Learning Yearning", "author": "Andrew Ng", "price": 750}
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/books")
def books_page():
    return render_template("books.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)