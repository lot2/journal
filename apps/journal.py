#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, request, g, session, redirect, url_for
import time
from apps import app

@app.route('/journal/list')
def list():
    return render_template("jList.html", title='jList')


@app.route('/journal/manage')
@app.route('/journal/manage/<date>')
def manage(date=None):
    if date == None:
        date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    return render_template("jManage.html", title='jManage', datestr=date)


@app.route('/journal/new')
def new():
    return render_template("jnew.html", title='New')


@app.route('/journal/new/doSave', methods=['GET', 'POST'])
def doSave():
    if request.method == 'POST':
        error = ""
        cx = g.db
        cu = cx.cursor()
        total_str = request.form["totalStr"]
        sub_str = request.form["subStr"]
        print total_str
        print sub_str
        # It needs time to achieve this function
        sql_user = "insert into journal_new(journal_date, user_id) values (%s,%s)"
        count = cu.execute(sql_user, total_str)
        if int(count) == 0:
            error = "UserName and Password is wrong."
    return error