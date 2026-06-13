
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('practice.db')
    conn.row_factory = sqlite3.Row  # HE LINE ADD KAR
    return conn

# Home Page - List all students
@app.route('/')
def index():
    db = get_db()
    students = db.execute("SELECT * FROM STUDENTS").fetchall()
    db.close()
    return render_template('Home.html', students=students)

# Add Student
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        marks = request.form['marks']
        db = get_db()
        db.execute("INSERT INTO STUDENTS (name, marks) VALUES (?, ?)", (name, marks))
        db.commit()
        db.close()
        return redirect('/')
    return render_template('add.html')

# Update Student
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_student(id):
    db = get_db()
    db.row_factory = sqlite3.Row
    
    if request.method == 'POST':
        new_name = request.form['name']
        db.execute("UPDATE STUDENTS SET name=? WHERE id=?", (new_name, id))
        db.commit()
        db.close()
        return redirect('/')
    
    student = db.execute("SELECT * FROM STUDENTS WHERE id=?", (id,)).fetchone()
    db.close()
    return render_template('update.html', student=student)

# Delete Student
@app.route('/delete/<int:id>')
def delete_student(id):
    db = get_db()
    db.execute("DELETE FROM STUDENTS WHERE id=?", (id,))
    db.commit()
    db.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)