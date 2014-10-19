#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, request, g, session, redirect, url_for
import sqlite3
from apps import app


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        cx = sqlite3.connect(g.db)
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