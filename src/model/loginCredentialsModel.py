from marshmallow import fields, Schema
import datetime
from . import db
from .userModel import UserModel

class LoginModel(db.Model):
    __tablename__='login_details'
    user_email = db.Column(db.String(128) , db.ForeignKey(UserModel.user_email), primary_key=True)
    user_password = db.Column(db.String(128))

    ## Whenever we create object of a class first thing which gets called is constructor.
    def __init__(self, login_obj):
        self.user_email = login_obj['user_email']
        self.user_password = login_obj['user_password']

        
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self, user_email):
        db.session.delete(user_email)
        db.session.commit()

    @staticmethod
    def getuser(user_email):
        return UserModel.query.get(user_email)

    @staticmethod
    def getPassword(user_id):
        return UserModel.query.get(user_id)

    @staticmethod
    def getAllUsers():
        return UserModel.query.all()

    # check if id is already present in db
    @staticmethod
    def checkUserId(user_email):
        return UserModel.query.filter_by(user_email = user_email).first()
    
    #delete user if user_id is present in db
    @staticmethod
    def deleteUser(user_email):
        return UserModel.query.filter(user_email==user_email).delete()
    
class LoginSchema(Schema):
    user_email = fields.Str()
    user_password = fields.Str()