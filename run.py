from flask import Flask, render_template
import time
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Home')


@app.route('/login')
def login():
    return render_template("login.html", title='Login')


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