#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import g
from apps import app
import os


app.debug = True

base_path = os.path.abspath(os.path.dirname(__file__))
JDB_NAME = os.path.join(base_path, 'JDB.db')

@app.before_request
def connect_db():
    #create a connect to the database
    g.db = JDB_NAME

@app.teardown_request
def teardown_request(exception):
    #any exception, need close the db connect
    None

@app.after_request
def close_db(response):
    #finally, need close the db connect and return the response
    return response

if __name__ == '__main__':
    app.run()