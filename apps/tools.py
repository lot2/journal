#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, request, g, session, redirect, url_for
from apps import app


def generateOne(param):
    #param1 = 2014-11-02,admin,
    #param2 = A1,A,A,A,A,A,A;B,B,B,B,B,B,B
    p = ""
    for i in param.split(","):
        p = p + "'"+i+"'" + ","
    val = "("+p[0: len(p)-1]+")"
    return val



def generateMany(param):
    #param1 = 2014-11-02,admin,
    #param2 = A1,A,A,A,A,A,A;B,B,B,B,B,B,B
    p1 = ""
    for j in param.split(";"):
        p = ""
        for k in j.split(","):
            p = p + "'"+k+"'"+","
        p1 = p1 + "("+p[0: len(p)-1]+")" + ","
    val = "["+p1[0: len(p1)-1]+"]"
    return val