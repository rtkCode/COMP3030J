from pet import app
from flask import redirect, render_template, url_for, session, request, jsonify
from flask_cors import CORS
from .models import User, Pet, Staff, Transcript
from pet import db
from werkzeug.security import generate_password_hash, check_password_hash
import os
import time
from .config import Config
import json
import re

CORS(app, supports_credentials=True)


@app.route("/login", methods=['POST'])
def login():
    if "username" in request.form.keys() and "password" in request.form.keys():
        username = request.form["username"]
        password = request.form["password"]
        user_in_db = User.query.filter(User.username == username).first()
        if not user_in_db:
            return jsonify({
                "code": 400,
                "msg": "Invalid username or password"
            })
        if (check_password_hash(user_in_db.password_hash, password)):
            return jsonify({
                "code": 200,
                "msg": "Login success"
            })
    return jsonify({
                "code": 400,
                "msg": "Invalid data"
            })


@app.route("/verifyUserId", methods=['POST'])
def verifyUserId():
    if "username" in request.form.keys():
        username = request.form["username"]
        user_in_db = User.query.filter(User.username == username).first()
        if not user_in_db:
            return jsonify({
                "code": 200,
                "msg": "Username is available"
            })
        else:
            return jsonify({
                "code": 400,
                "msg": "Username already exists"

            })
    elif "email" in request.form.keys():
    	email = request.form["email"]
    	email_in_db = User.query.filter(User.email == email).first()
    	if not email_in_db:
            return jsonify({
                "code": 200,
                "msg": "Email is available"
            })
        else:
            return jsonify({
                "code": 400,
                "msg": "Email already exists"

            })
    else:
        return jsonify({
            "code": 400,
            "msg": "Invalid data"                
        })

# @app.route ("/checkemail", methods=['POST'])  # line 44-53 inspiration from lecture 15 def check_username(), to check if email reused 
# def check_email():
#     chosen = request.form['email']
#     user_in_db = User.query.filter(User.email == chosen).first()
#     if not user_in_db:
#         return jsonify({'text': 'Email is available',
# 						'returnvalue': 0})
#     else:
#         return jsonify({'text': 'Sorry! Email is already taken',
# 						'returnvalue': 1})

# @app.route ("/checkphone", methods=['POST']) # line 55-64 inspiration from lecture 15 def check_username(), to check if the 2 password inputs are same
# def check_phone():
#     chosen = request.form['phone']
#     profile_in_db = Profile.query.filter(Profile.phone == chosen).first()
#     if not profile_in_db:
#         return jsonify({'text': 'Phone is available',
# 						'returnvalue': 0})
#     else:
#         return jsonify({'text': 'Sorry! Phone is already taken',
# 						'returnvalue': 1})
        

@app.route("/register", methods=['POST'])
def register():
    print(request.form)
    if "username" in request.form and "password" in request.form and "email" in request.form and "firstName" in request.form and "lastName" in request.form and "others" in request.form:
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        others = request.form["others"]

        email_in_db = User.query.filter(User.email == email).first()
        if email_in_db:
            return jsonify({
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

        if re.match('^[a-zA-Z]{2,10}$', firstName) is None:
            return jsonify({
                'code': 400,
                'msg': 'FirstName format wrong'
            })
        
        if re.match('^[a-zA-Z]{2,10}$', lastName) is None:
            return jsonify({
                'code': 400,
                'msg': 'LastName format wrong'
            })

        if re.match('^[a-zA-Z]{1}[a-zA-Z0-9\_]{3,15}$', username) is None:
            return jsonify({
                'code': 400,
                'msg': 'Username format wrong'
            })
        
        if re.match('^[a-zA-Z]{2,10}$', lastName) is None:
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
        user = User(username=username, email=email, password_hash=passw_hash, firstName=firstName, lastName=lastName, others=others)
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

# @app.route ("/profile", methods=['GET','POST']) # line 78-103 code from lecture 13 def profile(), I changed some columns that need in my database and website. 
# def profile():
#     form = ProfileForm()
#     if not session.get("USERNAME") is None:
#         if form.validate_on_submit():
#             user = User.query.filter(User.username == session.get("USERNAME")).first()
#             stored_profile = Profile.query.filter(Profile.user_id==user.id).first()
#             if not stored_profile:
#                 profile = Profile(dob=form.dob.data,phone=form.phone.data,gender=form.gender.data,user_id=user.id)
#                 db.session.add(profile)
#             else:
#                 stored_profile.dob = form.dob.data
#                 stored_profile.gender = form.gender.data
#                 stored_profile.phone = form.phone.data
#             db.session.commit()
#             return redirect(url_for('personal'))
#         else:
#             user = User.query.filter(User.username == session.get("USERNAME")).first()
#             stored_profile = Profile.query.filter(Profile.user_id==user.id).first()
#             if not stored_profile:     
#                 return render_template('profile.html', title='Add your profile',form=form)
#             else:
#                 form.dob.data = stored_profile.dob
#                 form.gender.data = stored_profile.gender
#                 form.phone.data = stored_profile.phone 
#                 return render_template('profile.html', title='Modify your profile',form=form)
 

# @app.route ("/personal", methods=['GET','POST']) # line 110-129 inspiration from lecture 15 def profile() and def post()
# def personal():
#     if not session.get("USERNAME") is None:
#         user = User.query.filter(User.username == session.get("USERNAME")).first()
#         profile = Profile.query.filter(Profile.user_id == user.id).first()
#         posts = Post.query.filter(Post.user_id==user.id).all()
#         if profile is None:
#             flash("You need to add your profile first!")
#             return redirect(url_for('profile',user=user))
#         else:
#             if profile.gender=='0':
#                 profile.gender = 'Male'
#             else:
#                 profile.gender = 'Female' 
#             prev_posts = {}
#             l = len(posts)
#             for i in range(l):
#                 str1 = str(posts[i].timestamp).split('.')
#                 prev_posts[i] = (posts[i].title, str1[0],posts[i].reply,posts[i].id)         
#             return render_template('personal.html',user=user,profile=profile,prev_posts=prev_posts)       

# @app.route ("/makepost", methods=['GET','POST'])   # line 127-140 code from lecture 13 def makepost()
# def makepost():
#     form = PostForm()
#     if not session.get("USERNAME") is None:
#         user = User.query.filter(User.username == session.get("USERNAME")).first()
#         if form.validate_on_submit():
#             post = Post(title=form.title.data,body=form.body.data,user_id=user.id,good=0,reply=0)
#             db.session.add(post)
#             db.session.commit()
#             flash('Post uploaded and saved')
#             return redirect(url_for('makepost'))
#         else:            
#             prev_posts = Post.query.filter(Post.user_id == user.id).all() 
#             return render_template('post.html', title='Add your posts',prev_posts=prev_posts,form=form,user=user)

@app.route ("/logout") # line 152-155 code from lecture 13 def logout()
def logout():
    session.pop("USERNAME",None)
    return redirect(url_for('login'))    

# @app.route("/showpost", methods=['GET','POST'])
# def showpost():
#     if not session.get("USERNAME") is None:#line 149-150 inspiration from lecture 15 line 99-100. 
#         user_in_db = User.query.filter(User.username == session.get("USERNAME")).first()
#         po = Post.query.filter().all()
#         posts = {}
#         l = len(po)
#         for i in range(l):
#             user = User.query.filter(User.id == po[i].user_id).first()
#             str1 = str(po[i].timestamp).split('.')
#             posts[i] = (po[i].title, user.username, str1[0],po[i].reply)
#         return render_template('showpost.html', user=user_in_db,posts=posts,author=user)


# @app.route("/postdetails/<post_title>", methods=['GET','POST'])  # line 161-187 from lecture 15 def post() and def profile()
# def postdetails(post_title):
#     form = ReplyForm()
#     if not session.get("USERNAME") is None:#line 164-166 inspiration from lecture 15 line 99-100.
#         user_now = User.query.filter(User.username == session.get("USERNAME")).first()
#         post = Post.query.filter(Post.title == post_title).first()
#         user = User.query.filter(User.id == post.user_id).first()  #line 167 inspiration from lecture 15 line 99-100.
#         time = str(post.timestamp).split('.')
#         b = False
#         if form.validate_on_submit():#line 170-171 inspiration from lecture 15 line 99-100.
#             reply = Reply(user_id=user_now.id,post_id=post.id,body=form.body.data)
#             post.reply = post.reply + 1
#             db.session.add(reply)
#             db.session.commit()
#             return redirect(url_for('postdetails',post_title=post_title))
#         else:                               
#             replys = Reply.query.filter(Reply.post_id == post.id).all()
#             prev_replys = {}
#             for i in range(len(replys)):
#                 user_reply = User.query.filter(User.id == replys[i].user_id).first()     
#                 if user_reply.id==user_now.id:
#                     b = True
#                 else:
#                     b = False          
#                 str1 = str(replys[i].timestamp).split('.')
#                 prev_replys[i] = (replys[i].body,user_reply.username,str1[0],replys[i].id,b)
#             return render_template('postdetail.html', post=post,post_time=time[0],user=user_now,author=user,form=form,prev_replys=prev_replys)

# @app.route("/deletepost/<id>",methods=['GET','POST'])
# def deletepost(id):
#     post = Post.query.filter(Post.id == id).first()
#     reply = Reply.query.filter(Reply.post_id == post.id).all()
#     for i in range(len(reply)):
#         db.session.delete(reply[i])
#     db.session.delete(post)
#     db.session.commit()
#     return redirect(url_for('personal'))

# @app.route("/deletereply/<id>",methods=['GET','POST'])
# def deletereply(id): 
#     reply = Reply.query.filter(Reply.id == id).first()
#     post = Post.query.filter(Post.id == reply.post_id).first()
#     post.reply = post.reply - 1 
#     db.session.delete(reply)
#     db.session.commit()
#     return redirect(url_for('postdetails',post_title=post.title))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
