#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
* Create by shylock on 2016/2/29
"""
from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)