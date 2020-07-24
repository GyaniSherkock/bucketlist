from flask import Flask
from src.views.bucket_operations_view import bucket_list_operations  as bucket_list_operations
from src.views.user_view import user_operations as user_operations
from src.config import app_config
from src.model import db
import os

def create_app(env_name):
    """
    Create app
    """
    # app initilization
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])
    db.init_app(app)

    app.register_blueprint(bucket_list_operations, url_prefix="/bucketlist/v1/task")
    app.register_blueprint(user_operations,url_prefix="/bucketlist/v1/user")

    @app.route("/ping", methods=["GET"])
    def index():
        return "Congratulations Ashish! Your service is up and running"


    return app
