"""
    1. Execute Some SQL Commands

        Object Relational Mapping (ORM)
        
        # 1: List Databases
        show databases;

        # 2: create your database
        create database gw2024pds;

        # 3: Select the database in which you wish to create your table
        use gw2024pds;

        # 4: Create table
        create table Customer(
            cid int primary key auto_increment,
            name varchar(256), 
            phone varchar(15), 
            email varchar(256),
            age int, 
            gender varchar(10)
        );

        # 5: Check if table is created in database
        show tables;

        # 6: Check the table structure
        describe Customer;


        # 7: Create Customer in Table
        insert into Customer values(null, 'John', 
            '+91 99999 11111', 'john@example,com', 20, 'male');

        insert into Customer values(null, 'Fionna', 
            '+91 99999 22222', 'fionna@example,com', 22, 'female');
            
        insert into Customer values(null, 'George', 
            '+91 99999 33333', 'george@example,com', 31, 'male');

        insert into Customer values(null, 'Ben', 
            '+91 99999 44444', 'ben@example,com', 19, 'male');

        # 8: Fetch Data from Customer
        select * from Customer;
        select * from Customer where email = 'john@example.com';
        select * from Customer where cid = 2;
        select * from Customer where cid = 2 and email = 'fionna@example.com';
        select * from Customer where gender = 'male' and age >=20;
        select name, phone from Customer where cid = 2;

        # 9: Update Operation
        update Customer set name = 'Johnnathon', 
            email = 'john.jj@example.com', age=45 where cid = 1;

        # 10: Delete Customer
        delete from Customer where cid = 1;

        create table Address(
            aid int primary key auto_increment,
            houseno varchar(256), 
            addressline varchar(15), 
            city varchar(256),
            state varchar(256),
            zipCode int, 
            landmark varchar(10)
        );

    2. Work with Virtual Env
        # 1: Create Virtual Env
        python -m venv myenv
        
        # 2: Activate Virtual Env
        (windows)
        .\myenv\Scripts\activate

        (mac/linux)
        source myenv/bin/activate

    3. Installation of Driver
        pip install mysql-connector-python

    4. SQL Connection with Python

    Customer: name, phone, email, age, gender etc.
    Address: houseno, addressline, city, state, zipCode, landmark
"""

class Customer:

    def __init__(self, name="", phone="", email="", age=0, gender=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.gender = gender

    def add_customer_details(self):
        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customer Email: ")
        self.age = int(input("Enter Customer Age: "))
        self.gender = input("Enter Customer Gender: ")

    def show(self):
        print("~~~~~~~~~~~~CUSTOMER~~~~~~~~~~~~~")
        print("{} | {} | {}".format(self.name, self.phone, self.email))
        print("{} | {}".format(self.age, self.gender))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


class Address:

    def __init__(self, houseno, addressline, city, state, zipCode, landmark):
        self.houseno = houseno
        self.addressline = addressline
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.landmark = landmark


# Create Object : Python
customer1 = Customer(name="John", phone="+91 99999 11111", email="john@example.com",
                     age=20, gender="male")

print(vars(customer1))

customer1.show()