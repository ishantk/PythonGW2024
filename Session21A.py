import datetime
import hashlib

class User:

    def __init__(self, name="", phone="", email="", password="", age=0, gender=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.age = age
        self.gender = gender
        self.created_on = datetime.datetime.now()

    def add_user_details(self):
        self.name = input("Enter Your Name: ")
        self.phone = input("Enter Your Phone: ")
        self.email = input("Enter Your Email: ")
        self.password = input("Enter Your Password: ").encode('utf-8')
        self.password = hashlib.sha256(self.password).hexdigest()
        self.age = int(input("Enter Your Age: "))
        self.gender = input("Enter Your Gender: ")
        

# user = User()
# user.add_user_details()
# print(vars(user))