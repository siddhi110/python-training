from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# DATABASE CONNECTION
def get_db():
    conn = sqlite3.connect('practice.db')
    conn.row_factory = sqlite3.Row
    return conn

# TABLE BANAVNARA CODE
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

create_table()

# GRADE CALCULATE KARNARE FUNCTION
def get_grade_data(marks):
    if marks >= 90:
        return {"grade": "Excellent", "class": "success", "icon": "🏆"}
    elif marks >= 75:
        return {"grade": "Good", "class": "primary", "icon": "👍"}
    elif marks >= 60:
        return {"grade": "Average", "class": "warning", "icon": "📊"}
    else:
        return {"grade": "Needs Help", "class": "danger", "icon": "⚠️"}

# HOME PAGE - SEARCH LA REDIRECT
@app.route("/")
def home():
    return redirect(url_for('search'))

# SEARCH PAGE - TABLE VIEW
@app.route("/search")
def search():
    q = request.args.get('q', '')
    conn = get_db()
    if q:
        students = conn.execute(
            "SELECT * FROM students WHERE name LIKE ? OR roll LIKE ? OR subject LIKE ?", 
            (f'%{q}%', f'%{q}%', f'%{q}%')
        ).fetchall()
    else:
        students = conn.execute("SELECT * FROM students ORDER BY id DESC").fetchall()
    
    stats = {'Excellent': 0, 'Good': 0, 'Average': 0, 'Needs Help': 0}
    for s in students:
        grade_info = get_grade_data(s['marks'])
        stats[grade_info['grade']] += 1
    
    conn.close()
    return render_template('search.html', students=students, q=q, stats=stats, get_grade_data=get_grade_data)

# GRID PAGE - CARD VIEW  
@app.route("/grid")
def grid_view():
    conn = get_db()
    students = conn.execute("SELECT * FROM students ORDER BY id DESC").fetchall()
    
    stats = {'Excellent': 0, 'Good': 0, 'Average': 0, 'Needs Help': 0}
    for s in students:
        grade_info = get_grade_data(s['marks'])
        stats[grade_info['grade']] += 1
    
    conn.close()
    return render_template('grid_test.html', students=students, stats=stats, get_grade_data=get_grade_data)

# EDIT STUDENT
@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit_student(id):
    conn = get_db()
    
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        marks = request.form['marks']
        subject = request.form['subject']
        
        conn.execute(
            "UPDATE students SET name=?, roll=?, marks=?, subject=? WHERE id=?",
            (name, roll, marks, subject, id)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('search'))
    
    student = conn.execute("SELECT * FROM students WHERE id=?", (id,)).fetchone()
    conn.close()
    return render_template("edit.html", student=student)

# DELETE STUDENT
@app.route("/delete/<int:id>")
def delete_student(id):
    conn = get_db()
    conn.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('search'))

if __name__ == "__main__":
    app.run(debug=True)