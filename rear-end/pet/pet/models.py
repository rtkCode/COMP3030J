from datetime import datetime
from pet import db

class User(db.Model): #line 4-13 code from lecture 15 model.py class User
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(16), index=True, unique=True)
    firstName = db.Column(db.String(10))
    lastName = db.Column(db.String(10))
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(40), index=True, unique=True)
    others = db.Column(db.String(140))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Pet(db.Model):#line 15-25 inspired from lecture 15 model.py class Post, I add some attributes.
    id = db.Column(db.Integer, primary_key = True) 
    nickname = db.Column(db.String(30))
    age = db.Column(db.Integer) 
    sex = db.Column(db.String(10))
    keeper_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Staff(db.Model):#line 27-35 code from lecture 15 model.py class Profile, I add an attribute called phone and decline the CV and image attributes.
    id = db.Column(db.Integer, primary_key = True) 
    sex = db.Column(db.String(10))
    job = db.Column(db.String(50), index=True)
    salary = db.Column(db.Integer, index=True) 
    phoneNumber = db.Column(db.Integer, index=True, unique=True) 
    age = db.Column(db.Integer)

    def __repr__(self):
        return '<Profile for user: {}, gender:{}, birthday:{}>'.format(self.dob,self.gender)        

# class Collection(db.Model):
#     id = db.Column(db.Integer, primary_key = True) 
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

class Transcript(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'))
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'))
    payment = db.Column(db.Integer, index=True)
    date = db.Column(db.Date, index=True)
    item = db.Column(db.String(50), index=True)


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pet_type = db.Column(db.String(10), index=True)
    emergency = db.Column(db.String(10), index=True)
    # staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'))
    symptom = db.Column(db.String(50), index=True)
    date = db.Column(db.Date, index=True)
    location = db.Column(db.String(50), index=True)
    message = db.Column(db.String(250), index=True)
