import sys
from functools import wraps

from flask import render_template, request, Flask, session, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_socketio import SocketIO
from flask_ngrok import run_with_ngrok
from pandas import DataFrame
import unicodedata as ud
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.config["Secret_Key"] = "6a79852e71abd3dc5e4d#"
#megrun_with_ngrok(app)
app.debug = True
app.secret_key = "AsdHahD12@!#@3@#@#554"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSORD'] = ''
app.config["MYSQL_DB"] = 'register'
app.config["SQLALCHEMY_DATABASE_URL"] = "http://localhost/phpmyadmin/tbl_structure.php?db=register&table=register"
app.config["MYSQL CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)
socketio = SocketIO(app)

def is_logged_in(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if "logged in" in session:
            return f(*args,*kwargs)
        else:
            flash("Unauthorized, Please log in","Danger")
            return redirect(url_for("index"))
    return wrap

def not_logged_in(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if "logged in" in session:
            return f(*args,*kwargs)
        else:
            flash("Unauthorized", "danger")
            return redirect(url_for("index"))
    return wrap

@app.route("/", methods=(["GET", "POST"]))
def index():
    # form = loginform()
    try:
        con = mysql.connection.cursor()
        print("Connected to database")
    except Exception as e:

        sys.exit(e)
    # cur = con.cursor()
    con.execute("SELECT * FROM register")
    data = DataFrame(data=con.fetchall())

    if request.method == "POST":

        username = request.form['username']
        password = request.form["evoc_id"]
        c_password = request.form['confirm_evoc_id']
        cur = mysql.connection.cursor()

        if username in list(data[0]):
            if password not in list(data[1]):
                if password in c_password:
                    flash("You need to log in")
                    return render_template("login.html")

            flash('User already exist')
            return render_template('index_a.html')
        else:
            if password == c_password:
                cur.execute("INSERT INTO register(username,password,c_password) VALUES (%s,%s,%s)",
                         (username, password, c_password))
                mysql.connection.commit()
                cur.close()
            else:
                flash("Both evoc-id does no match")
                return render_template("index_a.html", output_data=data)
            # if cur.username != username:
            # flash("you writtern wrong evoc_id")

            flash("Submission-Successful")
            return render_template("index.html")
    return render_template("login.html")
@app.route("/abc",methods = (["Get","Post"]))
def login():
    # form = loginform()
    try:
        con = mysql.connection.cursor()
        print("Connected to database")
    except Exception as e:
        sys.exit(e)
    #cur = con.cursor()
    con.execute("SELECT * FROM register")
    data = DataFrame(data=con.fetchall())

    if request.method == "POST":

        username = request.form['username']
        password = request.form['evoc_id']
        #c_password = request.form['confirm_evoc_id']
        cur = mysql.connection.cursor()

        if username in list(data[0]):
            if int(password) not in list(data[1]):
                flash("the following evoc_id is wrong")
                return render_template("login.html")
            else:
                return render_template('index.html')
        else:
            flash("You need to sign up ")
            return render_template("login.html")

    return render_template('index.html')

@app.route("/out")
def logout():
    if 'password' in session:
        cur = mysql.connection.cursor()
        password = session['password']
        x = '0'
        cur.execute("UPDATE register SET online=%s WHERE password = %s", (x,password))
        session.clear()
        flash("You are logged out")
        return redirect(url_for('index'))
    return render_template("login.html")

@app.route('/User')
def socketMyApp():
    return render_template("course-single.html")

@app.route('/sign-in')
def Sing_in():
    return render_template("sign_in.html")


@app.route('/Chat', methods=["Get", "Post"])
def chatapp():
    # form = loginform()
    if request.method == "POST":
        Username = request.form['Username']
        Messages = request.form["Messages"]

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO chatbox(Username,Messages) VALUES (%s,%s)", (Username, Messages))
        mysql.connection.commit()
        cur.close()

        return render_template("new_chat.html")

    return render_template("new_chat.html")


def messagerecieved(methods=["Get", "Post"]):
    print("message was recieved")


@socketio.on('my event')
def handle_my_custom_event(json, methods=["Get", "Post"]):
    print("recieved my event" + str(json))
    socketio.emit("my response", json, callback=messagerecieved)
    D = {b'\\xF0\\x9F\\x98\\xA2': 2, b'\\xF0\\x9F\\x98\\x82': 1, b'\\xF0\\x9F\\x98\\x86': 2, b'\\xF0\\x9F\\x98\\x89': 1,
         b'\\xF0\\x9F\\x8D\\xB5': 2, b'\\xF0\\x9F\\x8D\\xB0': 4, b'\\xF0\\x9F\\x8D\\xAB': 2, b'\\xF0\\x9F\\x8D\\xA9': 2,
         b'\\xF0\\x9F\\x98\\x98': 1, b'\\xE2\\x98\\xBA': 33, b'\\xE2\\x98\\x95': 1}
    for k, v in D.items():
        k = k.decode('unicode-escape').encode('latin1').decode('utf8')
        try:
            n = ud.name(k)
        except ValueError:
            n = 'no such name'
        print(k, ascii(k), n)
    return str(json)


@app.route('/Proj', methods=["Get", "Post"])
def projects():
    return render_template("index_1.html")


if __name__ == '__main__':
    app.run()
