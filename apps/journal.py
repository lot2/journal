#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, request, g, session, redirect, url_for
import time
from apps import app, tools


@app.route('/journal/list')
def list():
    cx = g.db
    cu = cx.cursor()
    sql = "select a.*," \
          "replace(group_concat(case" \
          " when length(b.contents) > 40 then concat(substring(b.contents, 1, 60),'...') " \
          "else b.contents " \
          "end), ',', '<br/>') as content_str " \
          "from journal_new a left join journal_new_detail b ON a.journal_id = b.journal_id " \
          "where a.status != '0' and b.task_status != '0' " \
          "and a.user_id = %s " \
          "group by a.journal_date,a.user_id order by journal_id desc"
    param = (session["user_id"],)
    cu.execute(sql, param)
    journal_index = cu.fetchall()
    return render_template("jList.html", title='jList', journal_index=journal_index)


@app.route('/journal/manage')
@app.route('/journal/manage/<date>')
def manage(date=None):
    if date == None:
        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    cx = g.db
    cu = cx.cursor()
    sql = "select a.*, b.* from journal_new a left join journal_new_detail b ON a.journal_id = b.journal_id " \
          "where a.status != '0' and b.task_status != '0' " \
          "and a.journal_date = %s and a.user_id = %s order by b.task_id"
    param = (date, session["user_id"])
    cu.execute(sql, param)
    journal_list = cu.fetchall()
    return render_template("jManage.html", title='jManage', datestr=date, journal_list=journal_list)


@app.route('/journal/new')
def new():
    return render_template("jnew.html", title='New')


@app.route('/journal/new/doSave', methods=['GET', 'POST'])
def doSave():
    # if session["username"] == None:
    #     return redirect(url_for('index'))
    val = ""
    error = ""
    if request.method == 'POST':
        cx = g.db
        total_str = request.form["totalStr"]
        sub_str = int(request.form["subStr"])+1
        try:
            #查询登陆人的用户编号
            cu1 = cx.cursor()
            sql1 = "select user_id from sys_users where user_name =%s"
            param1 = session["username"]
            cu1.execute(sql1, (param1,))
            row1 = cu1.fetchone()
            #print row1["user_id"]

            #插入主表journal_new，传递参数为日志日期和用户编号
            cu2 = cx.cursor()
            sql2 = "insert into journal_new(journal_date, user_id) values (%s,%s)"
            param2 = (total_str, row1["user_id"])
            cu2.execute(sql2, param2)

            #查询当前插入到journal_new的自增长字段，以便插入到journal_new_detail的journal_id中
            cu3 = cx.cursor()
            sql3 = "select last_insert_id() curr"
            cu3.execute(sql3)
            row2 = cu3.fetchone()
            #print row2['curr']

            #插入数据至表journal_new_detail
            cu4 = cx.cursor()
            sql4 = "insert into journal_new_detail" \
                   "(journal_id, contents, issue, spend_time, schedule, problem, solution, remark)" \
                   " values (%s, %s, %s, %s, %s, %s, %s, %s)"
            param4 = []
            for k in range(1, sub_str):
                i = str(k)
                journal_id = int(row2['curr'])
                content = str(request.form["content_"+i])
                issue = str(request.form["issue_"+i])
                spend_time = str(request.form["spend_time_"+i])
                schedule = str(request.form["schedule_"+i])
                problem = str(request.form["problem_"+i])
                solution = str(request.form["solution_"+i])
                remark = str(request.form["remark_"+i])
                param4.append((journal_id, content, issue, spend_time, schedule, problem, solution, remark))
            n = cu4.executemany(sql4, param4)
        except Exception as e:
            error = e
        if int(n) > 0:
            print 'success'
            cx.commit()
            val = "1"
        else:
            print 'fail'
            cx.rollback()
            val = error
    return val