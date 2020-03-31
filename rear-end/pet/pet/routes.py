from pet import app
from flask import request, jsonify,g
from flask_cors import CORS
from .models import User, Pet, Transcript, Appointment, Employee
from pet import db
from werkzeug.security import generate_password_hash, check_password_hash
import os
import time
import datetime
from .config import Config
import json
import re
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from flask_httpauth import HTTPTokenAuth


auth = HTTPTokenAuth()
CORS(app, supports_credentials=True)


@app.route("/login", methods=['POST'])
def login():
    if "employee" in request.form.keys():
        employee = request.form["employee"]
        # print(employee)
        if "username" in request.form.keys() and "password" in request.form.keys() and employee == "0":
            username = request.form["username"]
            password = request.form["password"]
            
            user_in_db = User.query.filter(User.username == username).first()
            if not user_in_db:
                return jsonify({
                    "code": 400,
                    "msg": "Invalid username or password"
                })
            if (check_password_hash(user_in_db.password_hash, password)):
                token = generateToken(user_in_db.username,0)

                return jsonify({
                    "code": 200,
                    "msg": "Login success",
                    "token":token
                })
            else:
                return jsonify({
                    "code": 400,
                    "msg": "Invalid username or password"
                })
        elif "username" in request.form.keys() and "password" in request.form.keys() and employee == "1":
            username = request.form["username"]
            password = request.form["password"]
            employee_in_db = Employee.query.filter(Employee.username == username).first()
            if not employee_in_db:
                return jsonify({
                    "code": 400,
                    "msg": "Invalid username or password"
                })
            if (check_password_hash(employee_in_db.password_hash, password)):
                token = generateToken(employee_in_db.username,1)
            
                return jsonify({
                    "code": 200,
                    "msg": "Login success",
                    "token":token
                })
            else:
                return jsonify({
                    "code": 400,
                    "msg": "Invalid username or password"
                })
        else:
            return jsonify({
                "code": 400,
                "msg": "Invalid data"
        })

    else:
        return jsonify({
                "code": 400,
                "msg": "Invalid data"
        })

@app.route("/appointment", methods=['POST'])
@auth.login_required
def appointment():
    if "date" in request.form.keys() and "petType" in request.form.keys() and "symptom" in request.form.keys() and "location" in request.form.keys():
        date = request.form["date"]
        pet_type = request.form["petType"]
        location = request.form["location"]
        symptom = request.form["symptom"]
        message = request.form["message"]
        emergency = request.form["emergency"]
        user = g.user   
        real_date = datetime.datetime.strptime(date,'%Y-%m-%d').date()   
        appointment = Appointment(customer_id=user.id,date=real_date, pet_type=pet_type, location=location, emergency=emergency, symptom=symptom, message=message)
        db.session.add(appointment)
        db.session.commit()
        return jsonify({
            "code": 200,
            "msg": "Appointment success",
                
        })
        
    return jsonify({
                "code": 400,
                "msg": "Invalid data"
            })

@app.route("/verifyToken", methods=['POST'])
@auth.login_required
def verifyToken():
    return jsonify({
            "code": 200,
            "msg": "Verify sucess"
        })


@app.route("/verifyUserId", methods=['POST'])
def verifyUserId():
    if "username" in request.form.keys():
        username = request.form["username"]
        user_in_db = User.query.filter(User.username == username).first()
        if not user_in_db:
            return jsonify({
                "code": 201,
                "msg": "Username is available"
            })
        else:
            return jsonify({
                "code": 401,
                "msg": "Username already exists"

            })
    elif "email" in request.form.keys():
        email = request.form["email"]
        email_in_db = User.query.filter(User.email == email).first()
        if not email_in_db:
            return jsonify({
                "code": 202,
                "msg": "Email is available"
            })
        else:
            return jsonify({
                "code": 402,
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
    # print(request.form["username"])
    if "username" in request.form and "password" in request.form and "email" in request.form and "firstName" in request.form and "lastName" in request.form and "employee" in request.form and "others" in request.form:
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        others = request.form["others"]
        employee = request.form["employee"]
        if employee == "0":
            email_in_db = User.query.filter(User.email == email).first()
            user_in_db = User.query.filter(User.username == username).first()
            if user_in_db:			
                return jsonify({
                    'code': 400,
                    'msg': 'Username already exists'
                })
        else:
            email_in_db = Employee.query.filter(Employee.email == email).first()
            employee_in_db = Employee.query.filter(Employee.username == username).first()
            if employee_in_db:			
                return jsonify({
                    'code': 400,
                    'msg': 'Username already exists'
                })
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
    
        passw_hash = generate_password_hash(password)
        # print(employee)
        if employee == "1":
            emp = Employee(username=username, email=email, password_hash=passw_hash,firstName=firstName, lastName=lastName, others=others)
            db.session.add(emp)
            db.session.commit()
        else:
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

def generateToken(user,employee):
    expiration = 3600
    serializer = Serializer(Config.SECRET_KEY,expires_in=expiration) #有效时间为秒
    token = serializer.dumps({"username":user,"employee":employee}).decode("ascii") #解码形式再讨论
    return token

@auth.verify_token
def verify_token(token):   
    g.user = None 
    s = Serializer(Config.SECRET_KEY)
    try:
        data = s.loads(token)
    except SignatureExpired:
        return False
    except BadSignature:
        return False
    username = data["username"]
    if_employee = data["employee"]
    if not username or not if_employee:
        return False
    else:
        if if_employee == "1":
            g.user = Employee.query.filter(Employee.username == username).first()
            # print(1)
        else:
            g.user = User.query.filter(User.username == username).first() #g是存用户相关数据的
            # print(2)
        return True
    
@auth.error_handler
def error_handler():
    return jsonify({
            'code': 404,
            'msg': 'Unauthorized Operation'
        })


@app.route ("/profile",methods=['POST'])
@auth.login_required
def profile():
    user = g.user   
    # real_date = datetime.datetime.strptime(date,'%Y-%m-%d').date()  
    user_in_db = User.query.filter(User.username == user.username).first() 
    if user_in_db:
        appointment = Appointment.query.filter(Appointment.customer_id == user_in_db.id).all()
        appointment_list = []
        for item in appointment:
            list_item = {}
            list_item["id"] = item.id
            list_item["type"] = item.pet_type
            # list_item["petStatus"] = item.petStatus
            list_item["symptom"] = item.symptom
            list_item["date"] = str(item.date)
            list_item["location"] = item.location
            list_item["message"] = item.message
            list_item["emergency"] = item.emergency
            list_item["status"] = item.status
            list_item["attendingDoctor"] = item.attendingDoctor
            list_item["employeeId"] = item.employeeId
            list_item["operationTime"] = str(item.operationTime)
            list_item["dischargeDate"] = str(item.dischargeDate)
            appointment_list.append(list_item)
        user = {}
        user["username"] = user_in_db.username
        user["firstName"] = user_in_db.firstName
        user["lastName"] = user_in_db.lastName
        user["email"] = user_in_db.email
        return jsonify({
            "code": 200,
            "msg": "Success",
            "data":{
                "basic":user,
                "appointments":appointment_list
            }
                   
        })
    else:    
        return jsonify({
            "code": 400,
            "msg": "Invalid data"
        })

@app.route ("/updateProfile",methods=['PUT'])
@auth.login_required
def updateProfile():
    if "firstName" in request.form and "lastName" in request.form and "email" in request.form:
        user = g.user
        email = request.form["email"]
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        user_in_db = User.query.filter(User.username == user.username).first()
        email_in_db = User.query.filter(User.email == email).first()
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

        
        if re.match('^[a-zA-Z0-9\_\-\!\#\$\%\&\'\*\+\-\=\?\^\_\`\{\|\}\~\.]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$',email) is None:
            return jsonify({
                'code': 400,
                'msg': 'Email format wrong'
            })

        if user_in_db and email_in_db is None:
            user_in_db.firstName = firstName
            user_in_db.lastName = lastName
            user_in_db.email = email
            db.session.commit()

            return jsonify({
            "code": 200,
            "msg": "Success"        
        })

    return jsonify({
        "code": 400,
        "msg": "Failed"        
    })
        
@app.route ("/allAppointments",methods=['GET'])
@auth.login_required
def allAppointments():
    username = g.user.username
    employee_in_db = Employee.query.filter(Employee.username == username).first()
    user_in_db = User.query.filter(User.username == username).first()
    if employee_in_db and (not user_in_db):
        appointments = Appointment.query.filter().all()
        appointment_list = []
        for item in appointments:
            list_item = {}
            list_item["id"] = item.id
            list_item["type"] = item.pet_type
            # list_item["petStatus"] = item.petStatus
            list_item["symptom"] = item.symptom
            list_item["date"] = str(item.date)
            list_item["location"] = item.location
            list_item["message"] = item.message
            list_item["emergency"] = item.emergency
            list_item["status"] = item.status
            list_item["attendingDoctor"] = item.attendingDoctor
            list_item["employeeId"] = item.employee_id
            list_item["operationTime"] = str(item.operationTime)
            list_item["dischargeDate"] = str(item.dischargeDate)
            appointment_list.append(list_item)
        
        return jsonify({
            "code":200,
            "msg":"Success",
            "data":{
                "appointments":appointment_list
            }
        })
    if user_in_db:
        return jsonify({
            "code":401,
            "msg":"Unauthorized"
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

@app.route ("/logout",methods=['POST']) # line 152-155 code from lecture 13 def logout()
@auth.login_required
def logout():
    g.user = None
    # logout_user()
    return jsonify({
            "code": 200,
            "msg": "Log out sucess"
        })   


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
