from flask import Flask, render_template, request, session, redirect, url_for, escape
import time
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template("login.html", title='Login')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/reg')
def reg():
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

if __name__ == '__main__':
    app.run(debug=True)