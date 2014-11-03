#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, request, g, session, redirect, url_for
from apps import app


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #session['username'] = request.form['username']
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
        t = (user_name, password)
        sql_user = "select distinct user_id, user_name from journal.sys_users where status = 1 " \
                   "and user_name=%s and password=%s"
        count = cu.execute(sql_user, t)
        row = cu.fetchone()
        if int(count) > 0:
            error = ""
            session['username'] = row["user_name"]
            session['user_id'] = row['user_id']
        else:
            error = "UserName and Password is wrong."
    return error


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/session')
def get_all_session():
    return  render_template("get_sessions.html")