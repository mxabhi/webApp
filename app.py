import mysql.connector
from mysql.connector import errorcode
from flask import Flask, render_template, request, redirect, url_for, session
import db_connection

app = Flask(__name__)
app.secret_key = "secret-key"

# database connection configuration
TABLE_NAME = 'admins'
config = db_connection.connect_to_database()

# function to verify login credentials
def verify_login(username, password):
    try:
        # connect to the database
        conn = db_connection.connect_to_database()
   
        # execute SELECT query to verify login credentials
        cursor = conn.cursor()
        query = "SELECT * FROM {} WHERE username='{}' AND password='{}'".format(TABLE_NAME, username, password)
        cursor.execute(query)
        data = cursor.fetchone()
   
        if data is not None:
            return True
        else:
            return False

    except mysql.connector.Error as err:
        print(err)
        return False

    finally:
        # close database connection
        conn.close()

def get_students():
    try:
        # connect to the database
        conn = db_connection.connect_to_database() 
        
        # execute SELECT query to retrieve students list
        cursor = conn.cursor()
        query = "SELECT * FROM students"
        cursor.execute(query)
        students = cursor.fetchall()

        return students

    except mysql.connector.Error as err:
        print(err)
        return []

    finally:
        # close database connection
        conn.close()
# website homepage
@app.route('/')
def index():
    return render_template('index.html')


# login page route
@app.route('/login')
def login():
    return render_template('login.html')

# handle login form submission
@app.route('/login', methods=['POST'])
def login_submit():
    username = request.form['username']
    password = request.form['password']
    
    if verify_login(username, password):
        # set session variable and redirect to dashboard
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        # display error message and redirect to login page
        error_msg = "Invalid username or password. Please try again."
        return render_template('login.html', error_msg=error_msg)

# dashboard route
@app.route('/dashboard')
def dashboard():
    # check if user is logged in
    if 'username' in session:
        try:
            # connect to the database and execute SELECT query to fetch student data
            conn = db_connection.connect_to_database()
            cursor = conn.cursor()
            query = "SELECT * FROM students"
            cursor.execute(query)
            students = get_students() 
        except mysql.connector.Error as err:
            print(err)
            students = []
        finally:
            # close database connection and render dashboard template with student data
            conn.close()
            for student in students:
                print(student[1])
            return render_template('dashboard.html', students=students)
    else:
        # redirect to login page if user is not logged in
        return redirect(url_for('login'))
# add student page route
@app.route('/add-student')
def add_student():
    return redirect(url_for('dashboard'))

# handle add student form submission
@app.route('/add-student', methods=['POST'])
def add_student_submit():
    # get form data
    name = request.form['name']
    student_class = request.form['class']
    address = request.form['address']
    fee_paid_str = request.form['fee_paid']
    fee_pending_str = request.form['fee_pending']

    # validate fee_paid and fee_pending inputs
    try:
        fee_paid = float(fee_paid_str)
        fee_pending = float(fee_pending_str)
    except ValueError:
        error_msg = "Fee paid and fee pending must be numeric"
        return render_template('dashboard.html', error_msg=error_msg)

    # insert new student record into database
    try:
        # connect to the database
        conn = db_connection.connect_to_database() 

        # execute INSERT query
        cursor = conn.cursor()
        query = "INSERT INTO students (name, class, address, fee_paid, fee_pending) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (name, student_class, address, fee_paid, fee_pending))
        conn.commit()

        # display success message and redirect to dashboard
        success_msg = "Student added successfully"
        print(success_msg)
        students = get_students()
        return render_template('dashboard.html', students = students)


    except mysql.connector.Error as err:
        print(err)
        error_msg = "An error occurred while adding student"
        students = []
        return render_template('dashboard.html', students = students)

    finally:
        # close database connection
        conn.close()

# logout route
@app.route('/logout')
def logout():
    # clear session variable and redirect to login page
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

