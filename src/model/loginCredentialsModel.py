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
    
class LoginSchema(Schema):
    user_email = fields.Str()
    user_password = fields.Str()