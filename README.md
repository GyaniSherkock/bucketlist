# bucketlist
BucketList 


python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade


- Install all the required dependencies either in virtual environment or globally  
   `pip install -r requirements.txt` 

- In src/config.py, in 'execute_config dictionary', set 'change_config' : test_db_config
- Uncomment the line for importing test_db_config

- Each function name should start with 'test'

- Command for running the test case is       
   `pytest "name of the file"`

   Eg:

      pytest .tests\Test_batch_update.py
      (Runs particular test case)

      or
      
      pytest .tests\
      (Runs all the test cases)

- For Coverage.xml command is 
   `pytest --cov=./ --cov-report xml:coverage.xml`