"""
    Web Application Development with Flask
    https://flask.palletsprojects.com/en/3.0.x/

    1. Install Flask in Virtual Env
       pip install Flask

    2. Create Object of Flask

    3. Create a Function, with route as /

    4. In main function run the Flas App using run()

    5. Return the HTML webapge as a template from function
"""

from flask import *
import datetime
import hashlib
from Session21C import MongoDBHelper

# Create the Object of Flask
# Which represents a Web Application
web_app = Flask("Doctors App")
db_helper = MongoDBHelper()

@web_app.route("/") # Decorator
def index():

    # either you can return plain text
    # message = "Welcome to Patient Management System. Its {}".format(datetime.datetime.now())

    # OR you can return HTML
    message = """
    <html>
    <head>
        <title>Doctors App</title>
    </head>
    <body>
        <center>
            <h3>Welcome to Doctors Appm</h3>
        </center>
    </body>
    </html>
    """

    # return message

    # render_template is used to return web pages (html pages)
    return render_template("index.html")

@web_app.route("/register")
def register():
    return render_template("register.html")

@web_app.route("/add-user", methods=["POST"])
def add_user_in_db():

    # Create a Dictionary with Data from HTML Register Form
    user_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
        "created_on": datetime.datetime.now()
    }

    db_helper.collection = db_helper.db["users"]
    # Save user in DataBase i.e. MongoDB
    result = db_helper.insert(user_data)
    # message = "Welcome to Home Page. User ID is: {}".format(result.inserted_id)
    # return message

    # Write the data in the Session Object
    # This data can now be used anywhere in the project
    session['name'] = user_data["name"]
    session['email'] = user_data["email"]

    # return render_template("home.html", name=session['name'], email=session['email'])
    return render_template("home.html", name=session['name'], email=session['email'])

@web_app.route("/fetch-user", methods=["POST"])
def feth_user_from_db():

    # Create a Dictionary with Data from HTML Register Form
    user_data = {
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
    }

    db_helper.collection = db_helper.db["users"]
    # Fetch user in DataBase i.e. MongoDB
    result = db_helper.fetch(query=user_data)

    print("result:", result)
    
    if len(result)>0:
        user_data = result[0] # Get the dictionary from List 
        session['email'] = user_data["email"]
        session['name'] = user_data["name"]
        return render_template("home.html", name=session['name'], email=session['email'])
    else:
        return "User Not Found. Please Try Again"


@web_app.route("/add-patient", methods=["POST"])
def add_patient_in_db():

    # Create a Dictionary with Data from HTML Register Form
    patient_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "gender": request.form["gender"],
        "age": int(request.form["age"]),
        "address": request.form["address"],
        "doctor_email": session['email'],
        "doctor_name": session['name'],
        "created_on": datetime.datetime.now()
    }

    db_helper.collection = db_helper.db["patients"]
    # Save Patient in DataBase i.e. MongoDB
    result = db_helper.insert(patient_data)
    message = "Patient Added Successfully"
    return message

@web_app.route("/fetch-patients")
def fetch_patients_from_db():

    # Create a Dictionary with Data from HTML Register Form
    user_data = {
        "doctor_email": session["email"]
    }

    db_helper.collection = db_helper.db["patients"]
    # Fetch user in DataBase i.e. MongoDB
    result = db_helper.fetch(query=user_data)

    print("result:", result)
    
    if len(result)>0:
        print(result)
        return "Patients Fetched"
    else:
        return "Patients Not Found. Please Try Again"


def main():

    # In order to use Session Tracking, create a Secret Key
    web_app.secret_key = "doctors-app-key-v1"

    # Run the App infinitely, till user wont quite
    web_app.run()
    # web_app.run(port=5001) # optionally you can give the port number

if __name__ == "__main__":
    main()