# Customer Object: name, phone, email, age, gender, created_on

"""
    create table Customer(
        cid int primary key auto_increment,
        name varchar(256),
        phone varchar(15),
        email varchar(256),
        age int,
        gender varchar(20),
        created_on datetime
    );

"""

import datetime

class Customer:
    
    def __init__(self, cid=0, name="", phone="", email="", age=0, gender=""):
        self.cid = cid
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.gender = gender
        self.created_on = datetime.datetime.now()

    def add_customer_details(self):
        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customer Email: ")
        self.age = int(input("Enter Customer Age: "))
        self.gender = input("Enter Customer Gender: ")
        # we will not get input for created_on
        # created_on is a system date time stamp


    def update_customer_details(self):
        name = input("Enter Customer Name: ")
        if len(name) != 0:
            self.name = name

        phone = input("Enter Customer Phone: ")
        if len(phone) != 0:
            self.phone = phone

        email = input("Enter Customer Email: ")
        if len(email) != 0:
            self.email = email
        
        age = input("Enter Customer Age: ")
        if len(age) != 0:
            self.age = int(age)

        gender = input("Enter Customer Gender: ")
        if len(gender) != 0:
            self.gender = gender
            
    def show(self):
        print("~~~~~~~~~~~~CUSTOMER~~~~~~~~~~~~~")
        print("Customer ID: {}".format(self.cid))
        print("{} | {} | {}".format(self.name, self.phone, self.email))
        print("{} | {} | {}".format(self.age, self.gender, self.created_on))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")