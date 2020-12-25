from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.secret_key = "Trapezium!1"
# SqlAlchemy Database Configuration With Mysql
USER = os.getenv('DB_USER')
PASSWORD = os.environ.get('DB_PASS')
DB = os.environ.get('DB')
HOST = os.environ.get('HOST')
connectionstring = "mysql://"+USER+":"+PASSWORD+"@"+HOST+"/"+DB
app.config['SQLALCHEMY_DATABASE_URI'] = connectionstring
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


def db_init(host, user, passwd, db):
    """
    Initialize the database by creating products table
    """
    global conn
    try:
        conn = db.connect(host=host, user=user, passwd=passwd, db=db)
        cur = conn.cursor()
        cur.execute("show tables like 'employees'")
        if not cur.rowcount:
            cur.execute("create table products(id INT(10) NOT NULL AUTO_INCREMENT, name VARCHAR(30) NOT NULL, email VARCHAR(30) NOT NULL,phone VARCHAR(30) NOT NULL, CONSTRAINT id_pk PRIMARY KEY (id))")
            conn.commit()
            conn.close()
        else:
            print("Database table already present")
    except Exception as msg:
        print("Exception while initializing database : %s" % msg)

# Creating model table for our CRUD database


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, name, email, phone):

        self.name = name
        self.email = email
        self.phone = phone


# This is the index route where we are going to
# query on all our employee data
@app.route('/')
def Index():
    all_data = Data.query.all()

    return render_template("index.html", employees=all_data)


@app.route('/test')
def pytest():
    return jsonify({'Site': 'Up'})


# this route is for inserting data to mysql database via html forms
@app.route('/insert', methods=['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        my_data = Data(name, email, phone)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

        return redirect(url_for('Index'))


# this is our update route where we are going to update our employee
@app.route('/update', methods=['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']

        db.session.commit()
        flash("Employee Updated Successfully")

        return redirect(url_for('Index'))


# This route is for deleting our employee
@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")

    return redirect(url_for('Index'))


if __name__ == "__main__":
    db_init(host=HOST, user=USER, passwd=PASSWORD, db=DB)
    app.run(debug=True)
