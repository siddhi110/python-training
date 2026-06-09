import flask
import sqlite3
app = flask.Flask(__name__)

def get_db():
    db = sqlite3.connect('practice.db')
    return db

def init_db():
    db = get_db()
    db.execute("CREATE TABLE IF NOT EXISTS STUDENTS (id INTEGER, name TEXT)")
    db.commit()
    db.close()

init_db()

@app.route('/')
def home():
    return "Database ready"

app.run(debug=True)