from flask import request, Response, Blueprint, jsonify
from src.model.taskModel import TaskModel , TaskSchema
from src.model.userModel import UserModel,UserSchema
from src.model.loginCredentialsModel import LoginModel,LoginSchema
from src.util.service_util import custom_response
from sqlalchemy import create_engine
import json
import os

"""BluePrint"""
user_operations = Blueprint("user_operations", __name__)

"""Schemas"""
task_schema = TaskSchema()
login_schema = LoginSchema()
user_schema = UserSchema()


# API for signup of user
@user_operations.route("/sign_up", methods=["POST"])
def sign_up():
    req=request.get_json()
    # first check if user is allready present in table or not
    if(UserModel.query.filter_by(user_email=req['user_email']).first() is  None):
        # saving into user_table first
        usermodel = UserModel(req)
        usermodel.save()
        # creating custom object to select only few attributes from request and saving it in another model
        login_details = {}
        login_details['user_email']=req['user_email']
        login_details['user_password']=req['user_password']
        loginmodel=LoginModel(login_details)
        loginmodel.save()
        # print(req)
        return custom_response({"response": "User Created Successfully '~~' "}, 201) 
    else:
        return custom_response({"response":"User allready Exists. You can login directly !"},404)

@user_operations.route("/sign_in", methods=["POST"])
def sign_in():
    req = request.get_json()
    print(req)
    if(UserModel.query.filter_by(user_email=req['user_email']).first() is  None):
        return custom_response({"response":{"message":"You are not registered. Please register to application before sign in."}},400)
    # check in user_table and credentials_table whether this is a valid user name and password

    if(UserModel.checkUserId(req['user_email']) and LoginModel.checkUserId(req['user_email'])):
        if(req['user_password'] == LoginModel.getPassword(req['user_email']).user_password):
            return custom_response({"response":{"message":"You are logged in successfully"}},201) 
        else :
            return custom_response({"response":{"message":"Your password is incorrect. Please Try again"}},500)

    else:
        if(not req['user_email'].isspace() or req['user_email'] == None or not req['user_password'].isspace() or req['user_password'] == None):
            return custom_response({"response":{"message":"Please enter User Id and Password correctly"}},400)

        return custom_response({"response":{"message":"You are not registered. Please register to application before sign in."}},400)
