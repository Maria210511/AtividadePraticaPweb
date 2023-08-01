from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3


app = Flask(__name__)
app.secret_key = 'j@ni210511'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO users (username, password) VALUES (?,?)', (username, password))
        conn.commit()
        conn.close()

        flash('Usuário criado com sucesso!')
        return redirect(url_for('index'))
    return render_template('register.html')

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
init_db()

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', 
    (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:

        flash('Login realizado com sucesso!')
    else:
        flash('Usuário ou senha incorretos.')
    return redirect(url_for('index'))

if __name__ == "__main__"
app.run(
        debug = True,
        host= "0.0.0.0")
