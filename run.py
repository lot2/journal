from flask import Flask, render_template, request, session, redirect, url_for, escape, flash
import time
import sqlite3
app = Flask(__name__)

JDB_NAME = 'JDB.db'
#..\JetBrains\PyCharm 3.4.1\jre\jre\bin\JDB.db(the location)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        cx = sqlite3.connect(JDB_NAME)
        cx.row_factory = sqlite3.Row
        cu = cx.cursor()
        sql_user = "select * from sys_users where status = 1"
        cu.execute(sql_user)
        flag = 0
        if request.form['username'].strip() == '' or request.form['password'].strip() == '':
            error = 'UserName or Password cannot be empty.'
        else:
            for t in cu:
                if request.form['username'] == t['user_name'] and request.form['password'] == t['password']:
                    flag += 1
            if flag > 0:
                session['username'] = request.form['username']
                cx.close()
                return redirect(url_for('index'))
            else:
                error = 'UserName or Password is invalid.'
        cx.close()
    return render_template("login.html", title='Login', error_login=error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    error = None
    if request.method == 'POST':
        if request.form['password'] != request.form['password-repeat']:
            error = 'Passwords do not match.'
            return render_template("reg.html", title='Reg', error_reg=error)
        if request.form['username'].strip() == '':
            error = 'UserName cannot be empty.'
            return render_template("reg.html", title='Reg', error_reg=error)
        if request.form['password'] == '' or request.form['password-repeat'] == '':
            error = 'Password cannot be empty.'
            return render_template("reg.html", title='Reg', error_reg=error)
        cx = sqlite3.connect(JDB_NAME)
        cu = cx.cursor()
        user_name = request.form['username']
        password = request.form['password']
        for t in [(user_name, password), ]:
            sql_ins = "insert into sys_users(user_name,password) values (?,?)"
            cu.execute(sql_ins, t)
        cx.commit()
        session['username'] = request.form['username']
        #flash('Register Successfully.')
        cx.close()
        return redirect(url_for('index'))
    return render_template("reg.html", title='Reg')


@app.route('/new')
def new():
    return render_template("new.html", title='New')


@app.route('/jList')
def jList():
    return render_template("jList.html", title='jList')


@app.route('/jManage')
@app.route('/jManage/<date>')
def jManage(date=None):
    if date == None:
        date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    return render_template("jManage.html", title='jManage', datestr=date)


def db_create():
    cx = sqlite3.connect(JDB_NAME)
    cu = cx.cursor()
    sql_create = """create table if not exists sys_users (
    user_id integer primary key,
    user_group varchar(10),
    user_name varchar(30),
    password varchar(10),
    email varchar(50),
    telephone varchar(20),
    status varchar(2) default '1',
    create_date timestamp not null default current_timestamp
    )"""
    cu.execute(sql_create)
    cx.commit()
    cx.close()

if __name__ == '__main__':
    db_create()
    app.run(debug=True)