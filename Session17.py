"""
    Doctor’s App

    User is a Doctor
    Doctor should be able to add Patients
    Doctor should be able to add consultation of a patient

    Doctor -> User of Application
    Patient : pid, name, phone, email, dob, gender, created_on
    Consultation: cid, pid, remarks, medicines, next_followup, created_on

"""

import datetime


"""
    create table Patient(
        pid int primary key auto_increment, 
        name varchar(256), 
        phone varchar(20), 
        email varchar(256), 
        dob date, 
        gender varchar(20), 
        created_on datetime
    );

"""

class Patient:

    def __init__(self, pid=0, name="", phone="", email="", dob="", gender=""):
        self.pid = pid
        self.name = name
        self.phone = phone
        self.email = email
        self.dob = dob
        self.gender = gender
        self.created_on = datetime.datetime.now()

    def add_patient_details(self):
        self.name = input("Enter Patient Name: ")
        self.phone = input("Enter Patient Phone: ")
        self.email = input("Enter Patient Email: ")
        self.dob = input("Enter Patient DOB (yyyy-mm-dd): ")
        self.gender = input("Enter Patient Gender: ")


    def show(self):
        print("======Patient=======")
        
        patient = """
        {pid} | {name}  | {phone}
        {email} | {dob}
        {gender}| {created_on} 
        """.format_map(vars(self))

        print(patient)

        print("====================")
    