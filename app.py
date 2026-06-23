from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_grade_data(marks):
    if marks >= 90:
        return {'grade': 'A+', 'class': 'success'}
    elif marks >= 75:
        return {'grade': 'A', 'class': 'primary'}
    elif marks >= 60:
        return {'grade': 'B', 'class': 'info'}
    elif marks >= 40:
        return {'grade': 'C', 'class': 'warning'}
    else:
        return {'grade': 'F', 'class': 'danger'}


app.jinja_env.globals.update(get_grade_data=get_grade_data)

@app.route('/')
def home():
    return redirect('/search')

@app.route('/search')
def search():
    conn = get_db()
    q = request.args.get('q')
    
    if q:
        students = conn.execute(
            "SELECT * FROM students WHERE name LIKE ? OR roll LIKE ? OR subject LIKE ? ORDER BY id DESC",
            (f'%{q}%', f'%{q}%', f'%{q}%')
        ).fetchall()
    else:
        students = conn.execute("SELECT * FROM students ORDER BY id DESC").fetchall()
    
    conn.close()
    return render_template('search.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        subject = request.form['subject']
        marks = int(request.form['marks'])
        
        conn = get_db()
        conn.execute("INSERT INTO students (name, roll, subject, marks) VALUES (?, ?, ?, ?)",
                     (name, roll, subject, marks))
        conn.commit()
        conn.close()
        return redirect('/search')
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db()
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        subject = request.form['subject']
        marks = int(request.form['marks'])
        
        conn.execute("UPDATE students SET name=?, roll=?, subject=?, marks=? WHERE id=?",
                     (name, roll, subject, marks, id))
        conn.commit()
        conn.close()
        return redirect('/search')
    
    student = conn.execute("SELECT * FROM students WHERE id=?", (id,)).fetchone()
    conn.close()
    return render_template('edit.html', student=student)

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/search')

if __name__ == '__main__':
    app.run(debug=True)