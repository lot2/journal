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
        cu = cx.cursor()
        user_name = request.form['username']
        password = request.form['password']
        t = (user_name, password,)
        sql_user = "select 1 from sys_users where status = 1 and user_name=? and password=?"
        cu.execute(sql_user, t)
        if not cu.fetchone():
            error = "UserName and Password is wrong."
        cx.close()
    return error

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))