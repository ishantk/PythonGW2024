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

# Create the Object of Flask
# Which represents a Web Application
web_app = Flask("Doctors App")

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


def main():
    # Run the App infinitely, till user wont quite
    web_app.run()
    # web_app.run(port=5001) # optionally you can give the port number

if __name__ == "__main__":
    main()