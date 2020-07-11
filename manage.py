from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os
from src import db, create_app

os.environ["DATABASE_URL"]="postgres://postgres:Gyanish@4150@localhost:5432/bucket_list" 
os.environ["FLASK_ENV"]="development"

# os.environ["DATABASE_URL"]="postgres://postgres:ashish4150@database-1.cxt5wurz5hfp.us-east-2.rds.amazonaws.com:5432/shopping_centre_db" 
# os.environ["FLASK_ENV"]="production"

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)


migrate = Migrate(app=app, db=db)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()