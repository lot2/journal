#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import render_template, request, g, session, redirect, url_for
import sqlite3
from apps import app


@app.route('/user/reg', methods=['GET', 'POST'])
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
        #cx = sqlite3.connect(g.db)
        cu = g.db
        user_name = request.form['username']
        password = request.form['password']
        for t in [(user_name, password)]:
            sql_ins = "insert into sys_users(user_name,password) values (%s,%s)"
            cu.execute(sql_ins, t)
        cu.commit()
        session['username'] = request.form['username']
        #flash('Register Successfully.')
        cu.close()
        return redirect(url_for('index'))
    return render_template("reg.html", title='Reg')


@app.route('/user/existUser', methods=['GET', 'POST'])
def existUser():
    if request.method == "POST":
        error = ""
        cx = g.db
        cu = cx.cursor()
        user_name = request.form['username']
        t = (user_name)
        sql = "select 1 from sys_users where user_name=%s"
        cu.execute(sql, t)
        if cu.fetchone():
            error = "UserName already exists."
        cx.close()
    return error