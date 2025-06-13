#app.py
from flask import Flask, render_template , request , redirect, url_for, session
# import sqlite3
# This is a simple Flask web application that serves a form and processes the submitted data.
# Importing Flask and other necessary modules from the flask package.
# This is a simple Flask web application that serves a form and processes the submitted data.
# flask is a library — it gives you tools to build web apps.
# Flask is the main app builder (like your cooking pot 🍲).
# render_template is used to load HTML files from the templates/ folder.
app = Flask(__name__)
# __name__ is a special variable that tells Flask where to find the app.
app.secret_key = 'secret123'
# secret_key is used to secure the session data.
# This is a secret key used for session management. It should be kept secret in production.

user={
    'name': 'admin',
    'password': 'admin123'
}
# This is a dictionary that holds a username and password for authentication.

# def init_db():
#     # this function initializes the SQLite database.
#     conn = sqlite3.connect('database.db')
#     c= conn.cursor()

@app.route('/')
def home():
    return redirect(url_for('login'))

# @app.route('/') is a decorator that tells Flask what URL should trigger the function below.
# This function returns the form.html file when you visit the root URL.
@app.route('/signup' , methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == user['name']:
            return render_template('signup.html', error='Username already exists')
        else:
            user['name'] = username
            user['password'] = password
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method  == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == user['name'] and password == user['password']:
                session['username']= username
                return redirect(url_for('submit'))
        else:
            return render_template('login.html', error= 'invalid username or password')
    return render_template('login.html')



@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        phone = request.form['phone']
        email = request.form['email']
        city = request.form['city']
        return render_template('result.html', name=name, age=age, gender=gender,
                               phone=phone, email=email, city=city)
    # For GET, just show the form
    return render_template('form.html')


# @app.route('/') is a decorator that tells Flask what URL should trigger the function below.
# The home function returns a simple HTML message when you visit the root URL.

# @app.route('/hello/<name>')
# def hello(name):
#     return f"<h2>Hello, {name}!</h2>"
# This function takes a name from the URL and returns a greeting message.
# @app.route('/hello/<name>') creates a dynamic route that takes a name from the URL.
# The hello function uses render_template to load the hello.html file and passes the name variable to it.

# @app.route('/greet/<name>')
# def greet(name):
#     return render_template('hello.html', name=name)
# This function uses render_template to load the hello.html file and passes the name variable to it.
# The hello.html file is located in the templates/ folder.



if __name__ == "__main__":
    app.run(debug=True)
# This line checks if the script is being run directly (not imported).
# If it is, it starts the Flask app with debug mode enabled.