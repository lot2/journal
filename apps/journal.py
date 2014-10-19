#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template
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