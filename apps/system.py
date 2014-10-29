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
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template("login.html", title='Login')


@app.route('/system/textLogin', methods=['GET', 'POST'])
def textLogin():
    if request.method == 'POST':
        error = ""
        cx = g.db
        cx.row_factory = sqlite3.Row
        cu = cx.cursor()
        sql_user = "select * from sys_users where status = 1"
        cu.execute(sql_user)
        for t in cu:
            if request.form['username'] == t['user_name'] and request.form['password'] == t['password']:
                error = ""
            else:
                error = "Username or Password is wrong"
        cx.close()
    return error

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))