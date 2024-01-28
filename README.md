# Simwire-plugin

## Building Containers
You can build this application using `docker-compose up --build -d`.  
You do not need to rebuild the containers everytime to update the code on the server: `docker-compose up -d`.  
You can simply restart the debugger ( or what for it trigger the restart) if you are using Pycharm's debugger.


## running virtual environment
***Note: Remember to activate the virtual environment again whenever you work on your Flask project.***

### Using Windows

To set up a virtual environment for a Flask project, you can use Python's built-in `venv` module.  
Here are the steps:

1. Open a command prompt (cmd) or PowerShell.

2. Navigate to your project directory using the `cd` command:  
`cd path/to/your/project`  

3.  Create a virtual environment if you have not  created a virtual environment for your project.  
Replacing `venv` with your preferred virtual environment name:  
   `python3 -m venv venv`

4. Activate the virtual environment:
   `venv\Scripts\activate`
   After activation, your terminal prompt should change to indicate that the virtual environment is active.

5. Install Flask and its dependencies within the virtual environment:  
`pip install flask`

Now you have a virtual environment set up for your Flask project. 
You can start building your Flask application within this isolated environment.  
To deactivate the virtual environment, simply run:
`deactivate`

### Using Linux / Mac

To set up a virtual environment for a Flask project, you can use Python's built-in `venv` module.  
Here are the steps:

1. Open a terminal.

2. Navigate to your project directory using the `cd` command:  
`cd path/to/your/project`  

3. Create a virtual environment if you have not  created a virtual environment for your project.
Replacing `venv` with your preferred virtual environment name:  
`python3 -m venv venv`

4. Activate the virtual environment:
   `source venv/bin/activate`  
After activation, your terminal prompt should change to indicate that the virtual environment is active.

5. Install Flask and its dependencies within the virtual environment:  
`pip install flask`

Now you have a virtual environment set up for your Flask project. 
You can start building your Flask application within this isolated environment.  
To deactivate the virtual environment, simply run:
`deactivate`


## Running Web Service using container or IDE
### connect using pycharm
This requires .env.local to have: `MYSQL_PYCHARM_HOST=localhost` AND `RUN_WEB_USING_IDE=1`.
Our PyCharm is configured to run in debugger which as you can imagine greatly improved our development speed.
To make this work we run using application.py 

### connect using container
This requires .env.local to have `MYSQL_CONTAINER_HOST=mysql` and `RUN_WEB_USING_IDE=0`.
This way the container is connected to directly.

## how we update the requirements file locally
The below code controls the libraries which are installed in the containers and when the code is deployed to AWS EB.

`pip freeze > requirements.txt`  
***OR***  
`pip freeze | sed 's/==/>=/g' > requirements.txt` 



## Connecting to database container
These are the setting you will need to access the container locally.  
HOST = localhost  
User = root  
Password = MYSQL_ROOT_PASSWORD  
Database = MYSQL_DATABASE

### Run migrations
You need to be in the application directory (ie. same directory as app.py) to run the migrations
You simply need to run `flask db upgrade` to run all the migrations that you have missed since you last update.
This will also seed the database with data.  [Learn More](https://flask-migrate.readthedocs.io/en/latest)

***Note: Be sure to delete this username when in your production instance.***  
Login Username = `testing@testing.com`  
Login Password = `password`


### Seeding the database container
The database will be created automatically when the application is rebuild using the --build tag. However, the build does not seed the database with data. 
Checkout the migrations folder for working examples of how to create your own seeds. 


## Test Case
For running tests you simply need to be within the application directory (ie. same level as the "tests" folder)  
Then run `pytest` to run all test cases within the application including the test cases for plugins.