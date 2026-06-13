from flask import Flask, render_template, request, redirect, url_for
from practice import get_db

app = Flask(__name__)

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
    elif marks >= 50:
        return {"grade": "Average", "class": "warning", "icon": "📊"}
    else:
        return {"grade": "Needs Help", "class": "danger", "icon": "⚠️"}

@app.route("/")
def home():
    return redirect(url_for('search'))

@app.route("/search")
def search():
    q = request.args.get('q', '')
    conn = get_db()
    if q:
        students = conn.execute(
            "SELECT * FROM students WHERE name LIKE? OR subject LIKE? OR roll LIKE?", 
            (f'%{q}%', f'%{q}%', f'%{q}%')
        ).fetchall()
    else:
        students = conn.execute("SELECT * FROM students ORDER BY id DESC").fetchall()
    
    # GRADE AANI STATS CALCULATE KAR
    stats = {"Excellent": 0, "Good": 0, "Average": 0, "Needs Help": 0}
    student_list = []
    for s in students:
        grade_data = get_grade_data(s['marks'])
        stats[grade_data['grade']] += 1
        student_list.append(dict(s, **grade_data)) # student madhe grade data add kela
    
    conn.close()
    return render_template("search.html", students=student_list, q=q, stats=stats)

@app.route("/add", methods=['POST'])
def add_student():
    name = request.form['name']
    roll = request.form['roll']
    marks = request.form['marks']
    subject = request.form['subject']
    conn = get_db()
    conn.execute("INSERT INTO students (name, roll, marks, subject) VALUES (?,?,?,?)",
                 (name, roll, marks, subject))
    conn.commit()
    conn.close()
    return redirect(url_for('search'))

@app.route("/delete/<int:id>")
def delete_student(id):
    conn = get_db()
    conn.execute("DELETE FROM students WHERE id =?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('search'))

# BONUS: EDIT ROUTE
@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit_student(id):
    conn = get_db()
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        marks = request.form['marks']
        subject = request.form['subject']
        conn.execute("UPDATE students SET name=?, roll=?, marks=?, subject=? WHERE id=?",
                     (name, roll, marks, subject, id))
        conn.commit()
        conn.close()
        return redirect(url_for('search'))
    
    student = conn.execute("SELECT * FROM students WHERE id=?", (id,)).fetchone()
    conn.close()
    return render_template("edit.html", student=student)

if __name__ == "__main__":
    app.run(debug=True)