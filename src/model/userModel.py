from marshmallow import fields, Schema
from datetime import datetime
from . import db
import datetime


class UserModel(db.Model):
    __tablename__='user_table'
    user_email = db.Column(db.String(128), primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    date_of_birth = db.Column(db.DateTime)
    user_password = db.Column(db.String(128))
    mobile_number = db.Column(db.String(10))

    ## Whenever we create object of a class first thing which gets called is constructor.
    def __init__(self, user_obj):
        self.user_email = user_obj['user_email']
        self.first_name = user_obj['first_name']
        self.last_name = user_obj['last_name']
        self.date_of_birth = datetime.datetime.utcnow()
        self.user_password = user_obj['user_password']
        self.mobile_number = user_obj['mobile_number']

    @staticmethod
    def checkUserId(user_email):
        return UserModel.query.filter_by(user_email = user_email).first()
    
    #delete user if user_id is present in db
    @staticmethod
    def deleteUser(user_email):
        return UserModel.query.filter(user_email==user_email).delete() 

        
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self, user_email):
        db.session.delete(user_email)
        db.session.commit()
    
class UserSchema(Schema):
    user_email = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    date_of_birth = fields.DateTime(dump_only=True)
    user_password = fields.Str()
    mobile_number = fields.Str()