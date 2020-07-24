from marshmallow import fields, Schema
import datetime
from . import db
from .userModel import UserModel

class TaskModel(db.Model):
    __tablename__ = 'task_table'
    user_email = db.Column(db.String(128),db.ForeignKey(UserModel.user_email))
    task_id = db.Column(db.Integer, autoincrement=True,primary_key = True)
    task_name = db.Column(db.String(128))
    task_description = db.Column(db.String(128))
    task_start_date = db.Column(db.DateTime)
    task_complete_date = db.Column(db.DateTime)
    task_assignee = db.Column(db.String(128))
    
    
    ## Whenever we create object of a class first thing which gets called is constructor.
    def __init__(self, task_obj):
        self.user_email = task_obj['user_email']
        self.task_name = task_obj['task_name']
        self.task_description = task_obj['task_description']
        self.task_start_date = task_obj['task_start_date']
        self.task_complete_date = task_obj['task_complete_date']
        self.task_assignee = task_obj['task_assignee']


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self, task_id):
        db.session.delete(task_id)
        db.session.commit()
    
class TaskSchema(Schema):
    user_email = fields.Str()
    task_id = fields.Integer()
    task_name = fields.Str()
    task_description = fields.Str()
    task_start_date = fields.DateTime()
    task_complete_date = fields.DateTime()
    task_assignee = fields.Str()
    