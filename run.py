import os, sys
from src import create_app
from flask_cors import CORS
from sqlalchemy import create_engine


os.environ['DATABASE_URL'] = "postgres://postgres:Gyanish@4150@localhost:5432/bucket_list" 
os.environ['FLASK_ENV'] = "development"

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)
# mail = Mail(app)
CORS(app)

"""MAIN FUNCTION"""

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run(host="0.0.0.0", port=port)