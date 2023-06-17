# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    render = 'index.html'
    user = {
        'username': 'Nikita'
    }
    
    posts = [
        {
            'author': {'username': 'Name1'},
            'body': 'Beautiful day in Portland',
        },
        {
            'author': {'username': 'Name2'},
            'body': 'Beautiful day in Northland',
        },
        {
            'author': {'username': 'Name3'},
            'body': 'Beautifuld day in United States',
        }
    ]
    
    return render_template(render, title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember me {}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    
    return render_template('login.html', title='Sign In', form=form)
