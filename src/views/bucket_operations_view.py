from flask import request, Response, Blueprint, jsonify
from src.model.taskModel import TaskModel , TaskSchema
from src.model.userModel import UserModel,UserSchema
from src.model.loginCredentialsModel import LoginModel,LoginSchema
from src.util.service_util import custom_response
from sqlalchemy import create_engine
import json
import os

"""BluePrint"""
bucket_list_operations = Blueprint("bucket_list_operations", __name__)

"""Schemas"""
task_schema = TaskSchema()


## API to create a task
@bucket_list_operations.route("/create", methods=["POST"])
def create_task():
    req = request.get_json()
    taskmodel=TaskModel(req)
    taskmodel.save()
    print(req)
    return custom_response({"response": "Task Created Successfully '~~' "}, 201)


## API to get all task
@bucket_list_operations.route("/getall", methods=["GET"])
def get_all_task():
    task=TaskModel.query.all()
    result = task_schema.dump(task, many=True).data
    return custom_response({"response": result}, 201)
    
## API to update a task
@bucket_list_operations.route("/update/<task_id>", methods=["PUT"])
def update_task(task_id):
    id=task_id
    req = request.get_json()
    engine = create_engine(os.getenv("DATABASE_URL"))   
    engine.execute("update task_table set task_name=" + "'" + req["task_name"] + "',"
                + "task_description="
                + "'"
                + req["task_description"]
                + "',"
                + "task_start_date="
                + "'"
                + req["task_start_date"]
                + "',"
                + "task_complete_date="
                + "'"
                + req["task_complete_date"]
                + "',"
                + "task_assignee="
                + "'"
                + req["task_assignee"]
                + "'" + " where task_id = " + "'" + id + "'" 
                )
    return custom_response({"response": "Task Updated Successfully"}, 201)

## API to Delete a task
@bucket_list_operations.route("/delete", methods=["POST"])
def delete_task():
    req=request.get_json()
    engine = create_engine(os.getenv("DATABASE_URL"))
    if(TaskModel.query.filter_by(task_id=req['task_id']).first() is not None):
        engine.execute("delete from task_table where task_id = " + "'" + str(req["task_id"]) + "'")
        print(req)
        return custom_response({"response": "Task deleted successfully"}, 201)
    return custom_response({"response":"Requested Id is not present"},404)