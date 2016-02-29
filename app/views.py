#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
* Create by shylock on 2016/2/29
"""

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
