from flask import Flask, render_template
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

if __name__ == '__main__':
    app.run(debug=True)