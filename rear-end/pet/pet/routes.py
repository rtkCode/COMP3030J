from pet import app
from flask import request, jsonify,g
from flask_cors import CORS
from .key import key
from .models import User, Pet, Transcript, Appointment, Employee,Discussion
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
from sqlalchemy import or_, and_
from .mail import MailSender


auth = HTTPTokenAuth()
CORS(app, supports_credentials=True)


@app.route("/login", methods=['POST'])
def login():
    if "employee" in request.form.keys():
        employee = request.form["employee"]
        
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
        fake_date = datetime.datetime.strptime("1970-01-01",'%Y-%m-%d').date()  
        appointment = Appointment(customer_id=user.id,date=real_date, pet_type=pet_type, location=location, emergency=emergency, symptom=symptom, message=message,operationTime=fake_date,dischargeDate=fake_date)
        db.session.add(appointment)        
        db.session.commit()
        mail_sender = MailSender(user.email)
        mail_sender.send_appointment_mail()
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
            if not "IRC" in request.form:
                return jsonify({
                    'code': 400,
                    'msg': 'Lack of data'
                })
            IRC = request.form["IRC"]
            
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
            if IRC == key:
                emp = Employee(username=username, email=email, password_hash=passw_hash,firstName=firstName, lastName=lastName, others=others)
                db.session.add(emp)
                db.session.commit()
            else:
                return jsonify({
                    'code': 400,
                    'msg': 'register failed'
                 })
        else:
            user = User(username=username, email=email, password_hash=passw_hash, firstName=firstName, lastName=lastName, others=others)
            db.session.add(user)
            db.session.commit()
        
        # MailSender
        mail_sender = MailSender(email)
        mail_sender.send_register_mail()

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
    g.employee = None 
    if_employee = ""
    username = None
    s = Serializer(Config.SECRET_KEY)
    try:
        data = s.loads(token)
    except SignatureExpired:
        return False
    except BadSignature:
        return False
    username = data["username"]
    if_employee = data["employee"]
    # print(username,if_employee)
    if not username: 
        return False
    else:
        if if_employee == 1:
            g.employee = Employee.query.filter(Employee.username == username).first()
            
            # print(g.user.email)
        elif if_employee == 0:
            
            g.user = User.query.filter(User.username == username).first() #g是存用户相关数据的
            # print(g.user.email)
        return True
    
@auth.error_handler
def error_handler():
    return jsonify({
            'code': 404,
            'msg': 'Unauthorized Operation'
        })



@app.route ("/customerAppointments",methods=['GET'])
@auth.login_required
def customerAppointments():
    if g.user is not None:
        appointment = Appointment.query.filter(Appointment.customer_id == g.user.id).all()
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
            if item.emergency == "false":
                list_item["emergency"] = False
            elif item.emergency == "true":
                list_item["emergency"] = True
            if item.status == "":
                list_item["status"] = "Waiting"
            else:
                list_item["status"] = item.status
            if item.attendingDoctor == "":
                list_item["attendingDoctor"] = "Undetermined"
            else:
                list_item["attendingDoctor"] = item.attendingDoctor
            list_item["employeeId"] = item.employee_id
            if str(item.operationTime) == "1970-01-01":
                list_item["operationTime"] = "Undetermined"
            else:
                list_item["operationTime"] = str(item.operationTime)
            if str(item.dischargeDate) == "1970-01-01":
                list_item["dischargeDate"] = "Undetermined"
            else:
                list_item["dischargeDate"] = str(item.dischargeDate)
            appointment_list.append(list_item)
        return jsonify({
            "code": 200,
            "msg": "Success",
            "data":{
                "appointments":appointment_list
            }
                   
        })
    else:
        return jsonify({
            "code": 401,
            "msg": "Unauthorized"
                   
        })


@app.route ("/profile",methods=['GET'])
@auth.login_required
def profile():
    user = g.user   
    employee = g.employee
    user_in_db = None
    if g.user is not None:
        user_in_db = User.query.filter(User.username == user.username).first()
    # real_date = datetime.datetime.strptime(date,'%Y-%m-%d').date()  
    elif g.employee is not None:
        user_in_db = Employee.query.filter(Employee.username == employee.username).first()
    else:
        return jsonify({
            "code": 401,
            "msg": "Unauthorized"
                   
        })
    if user_in_db:
        
        user = {}
        user["username"] = user_in_db.username
        user["firstName"] = user_in_db.firstName
        user["lastName"] = user_in_db.lastName
        user["email"] = user_in_db.email
        return jsonify({
            "code": 200,
            "msg": "Success",
            "data":{
                "basic":user
                
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
        if not user:
            return jsonify({
            "code":401,
            "msg":"Unauthorized"
        })
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


@app.route("/allAppointments/<status>/<typ>/<emergency>/<location>/<sequence>", methods=['GET'])
@auth.login_required
def allAppointments(status="",typ="",emergency="",location="",sequence=""):
    employee_in_db = g.employee
    
    request_type = typ
    request_status = status
    request_sequence = sequence
    
    if employee_in_db:
        if request_type == "all":
            if request_status == "all":
                if emergency == "all":
                    if location == "all":
                        appointments = Appointment.query.filter().all()
                    else:
                        appointments = Appointment.query.filter(Appointment.location == location).all()
                else:
                    if location == "all":
                        appointments = Appointment.query.filter(Appointment.emergency == emergency).all()
                    else:
                        appointments = Appointment.query.filter(and_(Appointment.location == location,Appointment.emergency == emergency)).all()

            elif request_status == "Processing&Operating&Discharged":
                if emergency == "all":
                    if location == "all":
                        appointments = Appointment.query.filter(or_(Appointment.status == "Processing",Appointment.status == "Operating",Appointment.status == "Discharged")).all()
                    else:
                        appointments = Appointment.query.filter(and_(Appointment.location == location,or_(Appointment.status == "Processing",Appointment.status == "Operating",Appointment.status == "Discharged"))).all()
                else:
                    if location == "all":
                        appointments = Appointment.query.filter(and_(Appointment.emergency == emergency,or_(Appointment.status == "Processing",Appointment.status == "Operating",Appointment.status == "Discharged"))).all()
                    else:
                        appointments = Appointment.query.filter(and_(Appointment.location == location,Appointment.emergency == emergency,or_(Appointment.status == "Processing",Appointment.status == "Operating",Appointment.status == "Discharged"))).all()
            elif request_status == "Waiting":
                if emergency == "all":
                    if location == "all":
                        appointments = Appointment.query.filter(Appointment.status == "").all()
                    else:
                        appointments = Appointment.query.filter(and_(Appointment.location == location,Appointment.status == "")).all()
                else:
                    if location == "all":
                        appointments = Appointment.query.filter(and_(Appointment.emergency == emergency,Appointment.status == "")).all()
                    else:
                        appointments = Appointment.query.filter(and_(Appointment.location == location,Appointment.emergency == emergency,Appointment.status == "")).all()         
            else:
                if emergency == "all":
                    if location == "all":
                        appointments = Appointment.query.filter(Appointment.status == request_status).all()
                    else:
                        appointments = Appointment.query.filter(and_(Appointment.location == location,Appointment.status == request_status)).all()
                else:
                    if location == "all":
                        appointments = Appointment.query.filter(and_(Appointment.emergency == emergency,Appointment.status == request_status)).all()
                    else:
                        appointments = Appointment.query.filter(and_(Appointment.location == location,Appointment.emergency == emergency,Appointment.status == request_status)).all()
        elif request_type == "":
            appointments = Appointment.query.filter().all()
        else:
            if request_status == "all":
                if emergency == "all":
                    if location == "all":
                        appointments = Appointment.query.filter(Appointment.pet_type == request_type).all()
                    else:
                        appointments = Appointment.query.filter(and_(Appointment.location == location,Appointment.pet_type == request_type)).all()
                else:
                    if location == "all":
                        appointments = Appointment.query.filter(and_(Appointment.emergency == emergency,Appointment.pet_type == request_type)).all()
                    else:
                        appointments = Appointment.query.filter(and_(Appointment.location == location,Appointment.emergency == emergency,Appointment.pet_type == request_type)).all()
            elif request_status == "Processing&Operating&Discharged":
                if emergency == "all":
                    if location == "all":
                        appointments = Appointment.query.filter(and_(Appointment.pet_type == request_type,or_(Appointment.status == "Processing",Appointment.status == "Operating",Appointment.status == "Discharged"))).all()
                    else:
                        appointments = Appointment.query.filter(and_(Appointment.pet_type == request_type,Appointment.location == location,or_(Appointment.status == "Processing",Appointment.status == "Operating",Appointment.status == "Discharged"))).all()
                else:
                    if location == "all":
                        appointments = Appointment.query.filter(and_(Appointment.pet_type == request_type,Appointment.emergency == emergency,or_(Appointment.status == "Processing",Appointment.status == "Operating",Appointment.status == "Discharged"))).all()
                    else:
                        appointments = Appointment.query.filter(and_(Appointment.pet_type == request_type,Appointment.location == location,Appointment.emergency == emergency,or_(Appointment.status == "Processing",Appointment.status == "Operating",Appointment.status == "Discharged"))).all()
            elif request_status == "Waiting":
                if emergency == "all":
                    if location == "all":
                        appointments = Appointment.query.filter(and_(Appointment.pet_type == request_type,Appointment.status == "")).all()
                    else:
                        appointments = Appointment.query.filter(and_(Appointment.pet_type == request_type,Appointment.location == location,Appointment.status == "")).all()
                else:
                    if location == "all":
                        appointments = Appointment.query.filter(and_(Appointment.pet_type == request_type,Appointment.emergency == emergency,Appointment.status == "")).all()
                    else:
                        appointments = Appointment.query.filter(and_(Appointment.pet_type == request_type,Appointment.location == location,Appointment.emergency == emergency,Appointment.status == "")).all()
            else:
                if emergency == "all":
                    if location == "all":
                        appointments = Appointment.query.filter(and_(Appointment.pet_type == request_type, Appointment.status == request_status)).all()
                    else:
                        appointments = Appointment.query.filter(and_(Appointment.location == location,Appointment.pet_type == request_type,Appointment.status == request_status)).all()
                else:
                    if location == "all":
                        appointments = Appointment.query.filter(and_(Appointment.emergency == emergency,Appointment.pet_type == request_type,Appointment.status == request_status)).all()
                    else:
                        appointments = Appointment.query.filter(and_(Appointment.location == location,Appointment.emergency == emergency,Appointment.pet_type == request_type,Appointment.status == request_status)).all()
        

        appointment_list = []
        for item in appointments:
            list_item = {}
            list_item["id"] = item.id
            list_item["type"] = item.pet_type
            
            list_item["symptom"] = item.symptom
            list_item["date"] = str(item.date)
            list_item["location"] = item.location
            list_item["message"] = item.message
            if item.emergency == "false":
                list_item["emergency"] = False
            elif item.emergency == "true":
                list_item["emergency"] = True
            if item.status == "":
                list_item["status"] = "Waiting"
            else:
                list_item["status"] = item.status
            if item.attendingDoctor == "":
                list_item["attendingDoctor"] = "Undetermined"
            else:
                list_item["attendingDoctor"] = item.attendingDoctor
            list_item["employeeId"] = item.employee_id
            if str(item.operationTime) == "1970-01-01":
                list_item["operationTime"] = "Undetermined"
            else:
                list_item["operationTime"] = str(item.operationTime)
            if str(item.dischargeDate) == "1970-01-01":
                list_item["dischargeDate"] = "Undetermined"
            else:
                list_item["dischargeDate"] = str(item.dischargeDate)
            appointment_list.append(list_item)
        
        if request_sequence == "date":
            appointment_list.sort(key=lambda item:item["date"])
        return jsonify({
            "code":200,
            "msg":"Success",
            "data":{
                "appointments":appointment_list
            }
        })
    else:
        return jsonify({
            "code":401,
            "msg":"Unauthorized"
        })

@app.route ("/employeeAppointments",methods=['GET'])
@auth.login_required
def employeeAppointments():
    username = g.employee.username
    
    employee_in_db = Employee.query.filter(Employee.username == username).first()
     
    if employee_in_db:
        appointments = Appointment.query.filter(Appointment.employee_id == employee_in_db.id).all()
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
            if item.emergency == "false":
                list_item["emergency"] = False
            elif item.emergency == "true":
                list_item["emergency"] = True
            if item.status == "":
                list_item["status"] = "Waiting"
            else:
                list_item["status"] = item.status
            if item.attendingDoctor == "":
                list_item["attendingDoctor"] = "Undetermined"
            else:
                list_item["attendingDoctor"] = item.attendingDoctor
            list_item["employeeId"] = item.employee_id
            if str(item.operationTime) == "1970-01-01":
                list_item["operationTime"] = "Undetermined"
            else:
                list_item["operationTime"] = str(item.operationTime)
            if str(item.dischargeDate) == "1970-01-01":
                list_item["dischargeDate"] = "Undetermined"
            else:
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

@app.route ("/updateAppointment",methods=['PUT'])
@auth.login_required
def updateAppointment():
    user_in_db = ""

    # user type
    employee = False

    # Determine the user type
    if g.user is not None:
        user = g.user.username
        user_in_db = User.query.filter(User.username == user).first()
    elif g.employee.username is not None:
        user = g.employee.username
        user_in_db = Employee.query.filter(Employee.username == user).first()
        employee = True
    else:
        return jsonify({"code": 400, "msg": "User type invalid"})

    if "id" in request.form:
        id = request.form["id"]
        appointment = Appointment.query.filter(Appointment.id == id).first()

        customer = User.query.filter(User.id == appointment.customer_id).first()
        mail_sender = MailSender(customer.email)

        if not employee:
            if appointment.customer_id != user_in_db.id:
                return jsonify({"code": 400, "msg": "Failed"})

        # add employee name and id to appointments
        if employee:
            if appointment.employee_id != user_in_db.id:
                return jsonify({"code": 400, "msg": "Failed"})

            if appointment.employee_id is None:
                appointment.employee_id = user_in_db.id
                appointment.attendingDoctor = user_in_db.firstName + " " + user_in_db.lastName

        if "status" in request.form:
            status = request.form["status"]
            # for customer
            if not employee:
                if status == "Completed" and appointment.status == "Discharged":
                    appointment.status = status
                    db.session.commit()
                    mail_sender.send_finish_mail()
                    return jsonify({"code": 200, "msg": "Appointment completed"})
                elif status == "Canceled" and appointment.status == "":
                    appointment.status = status
                    db.session.commit()
                    mail_sender.send_cancel_mail()
                    return jsonify({"code": 200, "msg": "Appointment canceled"})
                else:
                    return jsonify({"code": 400, "msg": "Permission denied"})
            # for employee
            if employee:
                if status == "Processing" and appointment.status == "":
                    appointment.status = status
                    db.session.commit()
                    mail_sender.send_processing_mail()
                    return jsonify({"code": 200, "msg": "Appointment processing"})

                appointment_status_set = set(["Processing", "Operating", "Discharged"])
                request_status_set = set(["Discharged", "Operating", "Canceled"])

                if status in request_status_set and appointment.status in appointment_status_set:
                    appointment.status = status
                    db.session.commit()
                    if status == "Discharged":
                        mail_sender.send_discharge_mail()
                    elif status == "Operating":
                        mail_sender.send_operation_mail()
                    elif status == "Canceled":
                        mail_sender.send_cancel_mail()
                    return jsonify({"code": 200, "msg": "Operation success"})

        if "operationTime" in request.form and employee:
            operationTime = request.form["operationTime"]
            appointment.operationTime = datetime.datetime.strptime(operationTime, '%Y-%m-%d').date()
            mail_sender.send_operation_mail()
        if "dischargeDate" in request.form and employee:
            dischargeDate = request.form["dischargeDate"]
            appointment.dischargeDate = datetime.datetime.strptime(dischargeDate, '%Y-%m-%d').date()
            mail_sender.send_discharge_mail()
        db.session.commit()
        return jsonify({"code": 200, "msg": "Operation success"})

    else:
        return jsonify({"code": 400, "msg": "Failed"})


@app.route ("/deleteAppointment",methods=['PUT'])
@auth.login_required
def deleteAppointment():
    employee_in_db = g.employee
    user_in_db = g.user
    
    if employee_in_db and "id" in request.form:
        id = request.form["id"]
        appointment = Appointment.query.filter(Appointment.id == id).first()
        customer = User.query.filter(User.id == appointment.customer_id).first()
        mail_sender = MailSender(customer.email)
        if appointment.employee_id == employee_in_db.id:
            appointment.status = "Canceled"
            db.session.commit()
            
            mail_sender.send_cancel_mail()
            return jsonify({"code": 200, "msg": "Success"}) 
        else:
            return jsonify({"code": 200, "msg": "Failed"})
        

        
    elif user_in_db and "id" in request.form:
        id = request.form["id"]
        appointment = Appointment.query.filter(Appointment.id == id).first()
        
        mail_sender = MailSender(user_in_db.email)
        if appointment.customer_id == user_in_db.id and appointment.status == "":
            appointment.status = "Canceled"
            db.session.commit()
            mail_sender = MailSender(email)
            mail_sender.send_cancel_mail()
            return jsonify({"code": 200, "msg": "Success"}) 
        else:
            return jsonify({"code": 200, "msg": "Failed"})

    else:
        return jsonify({"code": 400, "msg": "Failed"})

@app.route ("/discussion",methods=['POST'])
@auth.login_required
def discussion():
    if "appointmentId" in request.form.keys() and "content" in request.form.keys():
        appointmentId = request.form["appointmentId"]
        post = request.form["content"]
        if g.employee is not None:
            username = g.employee.username
            employee_in_db = Employee.query.filter(Employee.username == username).first()
            appointment = Appointment.query.filter(Appointment.id == appointmentId).first()
            if(appointment == None or appointment.employee_id != employee_in_db.id):
                return jsonify({
                "code":401,
                "msg":"Unauthorized"
            })
        
            localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            discussion = Discussion(appointment_id=appointmentId, content=post, post_time=localtime, employee="ture")
            db.session.add(discussion)
            db.session.commit()

            return jsonify({
                "code":200,
                "msg":"Success"
            })

        elif g.user is not None:
            username_cus = g.user.username
            user_in_db = User.query.filter(User.username == username_cus).first()
            appointment = Appointment.query.filter(Appointment.id == appointmentId).first()
            if(appointment == None or appointment.customer_id != user_in_db.id):
                return jsonify({
                "code":401,
                "msg":"Unauthorized"
            })
        
            localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            discussion = Discussion(appointment_id=appointmentId, content=post, post_time=localtime, employee="false")
            db.session.add(discussion)
            db.session.commit()

            return jsonify({
                "code":200,
                "msg":"Success"
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

@app.route ("/discussion/<string:appointmentId>",methods=['GET'])
@auth.login_required
def getDiscussions(appointmentId):
    if g.user is not None:
        username_cus = g.user.username
        user_in_db = User.query.filter(User.username == username_cus).first()
        appointment = Appointment.query.filter(Appointment.id == appointmentId).first()
        if(appointment == None or appointment.customer_id != user_in_db.id):
            return jsonify({
            "code":401,
            "msg":"Unauthorized"
        })

    elif g.employee is not None:
        username = g.employee.username
        employee_in_db = Employee.query.filter(Employee.username == username).first()
        appointment = Appointment.query.filter(Appointment.id == appointmentId).first()
        if(appointment == None or appointment.employee_id != employee_in_db.id):
            return jsonify({
            "code":401,
            "msg":"Unauthorized"
        })

    else:    
        return jsonify({
            "code": 400,
            "msg": "Invalid data"
        })

    discussions = Discussion.query.filter(Discussion.appointment_id == appointmentId).all()
    discussion_list = []
    for item in discussions:
        list_item = {}
        list_item["id"] = item.id
        list_item["content"] = item.content
        list_item["postTime"] = item.post_time
        if item.employee == "false":
            list_item["employee"] = False
        else:
            list_item["employee"] = True
        discussion_list.append(list_item)

    return jsonify({
        "code":200,
        "msg":"Success",
        "data":{
            "discussions":discussion_list
        }
    })




@app.route ("/logout",methods=['POST']) # line 152-155 code from lecture 13 def logout()
@auth.login_required
def logout():
    g.user = None
    g.employee = None
    # logout_user()
    return jsonify({
            "code": 200,
            "msg": "Log out sucess"
        })   




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
