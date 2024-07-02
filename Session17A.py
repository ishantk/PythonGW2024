"""
    Doctor’s App

    User is a Doctor
    Doctor should be able to add Patients
    Doctor should be able to add consultation of a patient

    Doctor -> User of Application
    Patient : pid, name, phone, email, dob, gender, created_on
    Consultation: cid, pid, remarks, medicines, next_followup, created_on

"""

"""
    create table Consultation(
        cid int primary key auto_increment, 
        pid int, 
        remarks varchar(256), 
        medicines varchar(256), 
        next_followup datetime, 
        created_on datetime,
        FOREIGN KEY (pid) REFERENCES Patient(pid)
    );

"""

import datetime

class Consultation:

    def __init__(self, cid=0, pid=0, remarks="", medicines="", next_followup=""):
        self.cid = cid
        self.pid = pid
        self.remarks = remarks
        self.medicines = medicines
        self.next_followup = next_followup
        self.created_on = datetime.datetime.now()

    def add_connsulation_details(self):
        self.pid = input("Enter Patient ID: ")
        self.remarks = input("Enter Consultation Remarks: ")
        self.medicines = input("Enter Medicines: ")
        self.next_followup = input("Enter next_followup (yyyy-mm-dd hh:mm:ss): ")

    def show(self):
        print("======Consultation=======")
        
        consultation = """
        {cid} | {pid} 
        {remarks} | {medicines}
        {next_followup}| {created_on} 
        """.format_map(vars(self))

        print(consultation)

        print("====================")
    
