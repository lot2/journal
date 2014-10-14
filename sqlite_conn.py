#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

SQLITE_DATABASE = ''
# #set default encoding as UTF-8
# reload(sys)
# sys.setdefaultencoding('utf-8')

#convert the resultset from Tuolt to Dict
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_conn():
    conn = sqlite3.connect(SQLITE_DATABASE)
    conn.row_factory = dict_factory
    return conn


def close_conn(conn):
    conn.close()

#insert by strSql
def insert(conn, strSql):
    cu = conn.cursor()
    try:
        cu.execute(strSql)
    except sqlite3.Error, e:
        print 'Inster failed:', e.args[0]
        return
    conn.commit()

#Query by strSql
def query(conn, strSql):
    cu = conn.cursor()
    try:
        cu.execute(strSql)
    except sqlite3.Error, e:
        print 'Query failed:', e.args[0]
        return
    return cu.fetchall()

#Update by strSql
def update(conn, strSql):
    cu = conn.cursor()
    try:
        cu.execute(strSql)
    except sqlite3.Error, e:
        print 'Update failed:', e.args[0]
        return
    conn.commit()

#Delete by strSql
def delete(conn, strSql):
    cu = conn.cursor()
    try:
        cu.execute(strSql)
    except sqlite3.Error, e:
        print 'Delete failed:', e.args[0]
        return
    conn.commit()

# if __name__ == "__main__":
#     database = 'D:\Dev\ProjectGit\Monitor\Server\people.db'
#     conn = get_conn(database)
#     for person in query(conn, 'select * from person'):
#         print json.dumps(person)
#
#     close_conn(conn)