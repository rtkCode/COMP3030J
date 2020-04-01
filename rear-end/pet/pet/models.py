from pet import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(16), index=True, unique=True)
    firstName = db.Column(db.String(10))
    lastName = db.Column(db.String(10))
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(40), index=True, unique=True)
    others = db.Column(db.String(140))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    nickname = db.Column(db.String(30))
    age = db.Column(db.Integer) 
    sex = db.Column(db.String(10))
    keeper_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Staff(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    sex = db.Column(db.String(10))
    job = db.Column(db.String(50), index=True)
    salary = db.Column(db.Integer, index=True) 
    phoneNumber = db.Column(db.Integer, index=True, unique=True) 
    age = db.Column(db.Integer)

    
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True) 
    username = db.Column(db.String(25), index=True, unique=True)
    email = db.Column(db.String(40), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    firstName = db.Column(db.String(10))
    lastName = db.Column(db.String(10))
    others = db.Column(db.String(140))

    def __repr__(self):
        return '<Employee {}>'.format(self.username)


class Transcript(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'))
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'))
    payment = db.Column(db.Integer, index=True)
    date = db.Column(db.Date, index=True)
    item = db.Column(db.String(50), index=True)


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pet_type = db.Column(db.String(50), index=True)
    emergency = db.Column(db.String(10), index=True)
    status = db.Column(db.String(50), index=True, default="")
    symptom = db.Column(db.String(150), index=True)
    date = db.Column(db.Date, index=True)
    location = db.Column(db.String(50), index=True)
    message = db.Column(db.String(250), index=True)
    attendingDoctor = db.Column(db.String(50), index=True, default="")
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    operationTime = db.Column(db.Date, index=True)
    dischargeDate = db.Column(db.Date, index=True)
