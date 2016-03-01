#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
* Create by shylock on 2016/2/29
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from app import views, models
