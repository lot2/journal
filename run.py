#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import g
from apps import app
import MySQLdb
import os
from contextlib import closing

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

app.debug = True

base_path = os.path.abspath(os.path.dirname(__file__))
#JDB_NAME = os.path.join(base_path, 'JDB.db')


def connect_db():
    return MySQLdb.connect(host='127.0.0.1', user='root', passwd='1qaz@WSX', db='journal')


# def init_db():
#     with closing(connect_db()) as db:
#         for line in app.open_resource('schema.sql', mode='r'):
#             db.cursor().execute(line)
#         # with app.open_resource('schema.sql', mode='r') as f:
#         #     db.cursor().executescript(f.read())open('schema.sql', 'r')
#         db.commit()


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    #any exception, need close the db connect
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.after_request
def close_db(response):
    #finally, need close the db connect and return the response
    return response

if __name__ == '__main__':
    #init_db()
    app.run()