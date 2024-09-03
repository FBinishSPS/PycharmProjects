from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkeyyoucanmakeitwhateveryouwant'

def init_db():
    conn = sqlite3.connect('basic_flask.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        age INTEGER NOT NULL
    ) ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('welcome'))
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        age = request.form['age']

        # Database connection
        conn = sqlite3.connect('basic_flask.db')
        cursor = conn.cursor()

        # Insert user details into the users table
        cursor.execute('INSERT INTO users (username, password, age) VALUES (?, ?, ?)', (username, password, age))
        conn.commit()

        # Fetch the newly created user to log them in
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()

        # Log the user in by adding them to the session
        session['user'] = user[1]
        session['age'] = user[3]

        # Redirect to the welcome page
        return redirect(url_for('welcome'))

    # If the request method is GET, show the registration form
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('basic_flask.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        session['user'] = user[1]
        session['age'] = user[3]
        return redirect(url_for('welcome'))
    flash('Login Failed. Check your username and password.', 'danger')
    return redirect(url_for('login'))

@app.route('/welcome')
def welcome():
    if 'user' in session:
        user = session['user']
        age = session['age']
        return render_template('welcome.html', user=user, age=age)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('age', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()
    app.run(port=5000, debug=True)


@app.route('/calculator')
def calculator():
   return render_template('calculator.html')


@app.route('/calculator', methods=['POST'])
def calculator_post():
   num1 = float(request.form['num1'])
   num2 = float(request.form['num2'])
   operation = request.form['operator']

   if operation == '+':
       result = num1 + num2
   elif operation == '-':
       result = num1 - num2
   elif operation == '*':
       result = num1 * num2
   elif operation == '/':
       if num2 != 0:
           result = num1 / num2
       else:
           result = 'Error: Division by zero'
   else:
       result = 'Invalid operation'
   # check to see if the result is an integer
   if result.is_integer():
       result = int(result)
   return render_template('calculator.html', result=result)


