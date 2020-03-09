from pet import app
# from .form import LoginForm, SignUpForm, ProfileForm, PostForm, ReplyForm
from flask import flash,redirect,render_template,get_flashed_messages,url_for,session, request,jsonify
from .models import User,Pet,Staff,Transcript
from pet import db
from werkzeug.security import generate_password_hash, check_password_hash
import os
import time
from .config import Config
import json
import re

#http://www.pythondoc.com/flask-sqlalchemy/queries.html All the query, delete and other operations of database are learned from this website. 
#The structure of route function are learned from lecture 9
#The structure of route function that has parameters are learned from https://blog.csdn.net/weixin_36380516/article/details/80008496

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='Home')





@app.route ("/verifyUserId", methods=['POST'])    # line 33-42 code from lecture 15 def check_username()
def verifyUserId():
    json_data = request.get_data()
    data = json.loads(json_data,encoding="utf-8")      
    
    if data["username"] and data["email"]:
        username = data["username"]
        email = data["email"]
        user_in_db = User.query.filter(User.username == username).first()
        email_in_db = User.query.filter(User.email == email).first()
        if (not user_in_db) and (not email_in_db):
            return jsonify({
                "code": 200,
                "msg": "Username and Email is OK"                
            })
        else:
            return jsonify({
                "code": 400,
                "msg":"Username and Email already exists"

            })
    else:
        return jsonify({
            "code": 400,
            "msg": "Invalid data"                
        })



@app.route ("/register", methods=['GET','POST']) # line 67-77 inspiration from lecture 15 def signup()
def register():
    json_data = request.get_data()
    data = json.loads(json_data,encoding="utf-8")  
    print(data)
    if data:
        username = data["username"]
        password = data["password"]
        email = data["email"]
        firstName = data["firstName"]
        lastName = data["lastName"]
        others = data["others"]

        email_in_db = User.query.filter(User.email == email).first()
        if email_in_db:
            return  jsonify({
                'code': 400,
                'msg': 'Email already exists'
            })
        
        if re.match('^[a-zA-Z0-9\_\-\!\#\$\%\&\'\*\+\-\=\?\^\_\`\{\|\}\~\.]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$',email) is None:
            return jsonify({
                'code': 400,
                'msg': 'Email format wrong'
            })
        
        if len(password)<6 or len(password)>18:
            return jsonify({
                'code': 400,
                'msg': 'Password length wrong'
            })

        if re.match('^[a-zA-Z]{2,10}$',firstName) is None:
            return jsonify({
                'code': 400,
                'msg': 'FirstName format wrong'
            })
        
        if re.match('^[a-zA-Z]{2,10}$',lastName) is None:
            return jsonify({
                'code': 400,
                'msg': 'LastName format wrong'
            })

        if re.match('^[a-zA-Z]{1}[a-zA-Z0-9\_]{3,15}$',username) is None:
            return jsonify({
                'code': 400,
                'msg': 'Username format wrong'
            })
        
        if re.match('^[a-zA-Z]{2,10}$',lastName) is None:
            return jsonify({
                'code': 400,
                'msg': 'LastName format wrong'
            })


        user_in_db = User.query.filter(User.username == username).first()
        if user_in_db:			
            return jsonify({
                'code': 400,
                'msg': 'Username already exists'
            })


        passw_hash = generate_password_hash(password)
        user = User(username=username, email=email,password_hash=passw_hash,firstName=firstName,lastName=lastName,others=others)
        db.session.add(user)
        db.session.commit()
        return jsonify({
            'code': 200,
            'msg': 'register success'
        })
    else:
        return jsonify({
            'code': 400,
            'msg': 'register failure'
        })




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)