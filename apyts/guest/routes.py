from flask import Blueprint, render_template, redirect, session, flash, request, make_response
from flask.helpers import url_for
from werkzeug.utils import secure_filename
import os
from datetime import datetime
import random,string
from werkzeug.security import generate_password_hash,check_password_hash
from wtforms import form
from apyts.guest.forms import ContactForm, GreetUserForm
#from apyts import app,db


guests= Blueprint('guests',__name__)

@guests.route('/',methods=['GET','POST'])
@guests.route('/home/',methods=['GET','POST'])
def home():
    form=ContactForm()
    nowl = datetime.now()
    today= nowl.strftime("%d/%m/%Y %H:%M:%S")
    if request.method=='GET':
        return render_template('guest/index.html', form=form, today=today)
    else:
        if form.validate_on_submit():
            usname=form.name.data
            usemail=form.email.data
            usmessage=form.summary.data
            #today = date.today()
            details=[usname,usemail,usmessage,today,'**********']
            msg= open('message.txt', 'a')
            for i in details:
                msg.write(i)
                msg.write('\n')
            msg.close()
            #return redirect(url_for('guests.home'))
            flash(f'Thank You {usname}, message sent successfully.' , 'success')
            return redirect(url_for('guests.home'))
        else:
            usname=form.name.data
            #return render_template('guest/index.html', form=form)
            flash(f' Message not sent, kindly check your inputs.' , 'danger')
            return render_template('guest/index.html', form=form)

@guests.route('/hello/',methods=['GET','POST'])
def hello():
    form=GreetUserForm()
    if request.method=='GET':
        return render_template('guest/hello.html', form=form)
    else:
        if form.validate_on_submit():
            usname=form.username.data
            flash(f'You have been logged in {usname}' , 'success')
            return 'Successfule'
        else:
            return render_template('guest/hello.html', form=form)


# @guests.route('/',methods=['GET','POST'])
# @guests.route('/home/')
# def home():
#     form=ContactForm()
#     if request.method=='GET':
#         return render_template('guest/index.html', form=form)
#     else:
#         if form.validate_on_submit():
#             return redirect(url_for('guests.home'))
#         else:
#             #return render_template('guest/index.html', form=form)
#             return redirect(url_for('guests.home'))