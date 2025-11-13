import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.sql')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    messages = conn.execute('SELECT * FROM hello_world').fetchall()
    conn.close()
    return render_template('index.html', messages=messages)

@app.route('/add', methods=['POST'])
def add_message():
    message = request.form['message']
    conn = get_db_connection()
    conn.execute('INSERT INTO hello_world (message) VALUES (?)', (message,))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/clear', methods=['POST'])
def clear_messages():
    conn = get_db_connection()
    conn.execute('DELETE FROM hello_world')
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

if __name__ == '__main__':
    conn = sqlite3.connect('database.sql')
    conn.execute('CREATE TABLE IF NOT EXISTS hello_world (id INTEGER PRIMARY KEY AUTOINCREMENT, message TEXT)')
    conn.close()

    app.run(debug=True)
