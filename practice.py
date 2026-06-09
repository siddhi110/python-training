from flask import Flask, request, render_template_string

app = Flask(__name__)

# 1. get_db() function
def get_db():
    import sqlite3
    db = sqlite3.connect('practice.db')
    return db

# 2. init_db() apna table
def init_db():
    db = get_db()
    db.execute("CREATE TABLE IF NOT EXISTS STUDENTS (id INTEGER PRIMARY KEY, name TEXT)")
    db.commit()
    db.close()

init_db()

# 3. One SELECT route - Home page var data show karnar
@app.route('/')
def home():
    db = get_db()
    students = db.execute("SELECT * FROM STUDENTS").fetchall()
    db.close()

    return render_template_string('''
        <h1>Database Practice</h1>

        <h2>Add New Student</h2>
        <form method="POST" action="/add">
            <input name="name" placeholder="Student Name" required>
            <button type="submit">Add Student</button>
        </form>

        <h2>All Students</h2>
        {% if students %}
            {% for student in students %}
                <p>ID: {{student[0]}} | Name: {{student[1]}}</p>
            {% endfor %}
        {% else %}
            <p>Database madhe ajun koni nahi.</p>
        {% endif %}
    ''', students=students)

# 4. One INSERT route - Form se data taknar
@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    db = get_db()
    db.execute("INSERT INTO STUDENTS (name) VALUES (?)", (name,))
    db.commit()
    db.close()
    return "Student Added! <a href='/'>Go Back to Home</a>"

app.run(debug=True)