from Session17 import Patient
from Session17A import Consultation
from Session15A import Database
from tabulate import tabulate 

def main():
    print("=======================")   
    print("Welcome to Doctor's App")
    print("=======================")

    db = Database()

    while True:
        print("1: Add New Patient")
        print("2: Update Existing Patient")
        print("3: Delete Existing Patient")
        print("4: View Patient By Phone")
        print("5: View Patient By PID")
        print("6: View All Patients")
        print("0: To Quit App")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            patient = Patient()
            patient.add_patient_details()
            sql = "insert into Patient values(null, '{name}', '{phone}', '{email}', '{dob}', '{gender}', '{created_on}')".format_map(vars(patient))
            db.write(sql)
            print("Patient Created..")
        
        elif choice == 6:
            sql = "select * from Patient"
            rows = db.read(sql)

            columns = ["pid", "name", "phone", "email", "dob", "gender", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))
            
        elif choice == 0:
            break
        else:
            print("Inavlid Choice")


if __name__ == "__main__":
    main()