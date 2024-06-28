# customer management app

from Session15 import Customer
from Session15A import Database
from tabulate import tabulate       # pip install tabulate

def main():
    print("-------------------")
    print("WELCOME to CMS APP")
    print("-------------------")

    db = Database()

    while True:
        print("1: Add New Customer")
        print("2: Update Existing Customer")
        print("3: Delete Existing Customer")
        print("4: View Customer By Phone")
        print("5: View Customer By CID")
        print("6: View All Customers")
        print("0: To Quit App")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            customer = Customer()
            customer.add_customer_details()
            sql = "insert into Customer values(null, '{name}', '{phone}', '{email}', {age}, '{gender}', '{created_on}')".format_map(vars(customer))

            # sql = "insert into Customer values(null, '{}', '{}', '{}', {}, '{}', null)".format(customer.name, customer.phone, customer.email, customer.age, customer.gender)

            db.write(sql)
            print("[CMS App]", customer.name, "Saved in DataBase")

        elif choice == 2:
            cid = int(input("Enter Customer ID to Update: "))
            sql = "select * from Customer where cid = {}".format(cid)
            rows = db.read(sql)

            columns = ["cid", "name", "phone", "email", "age", "gender", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))

        elif choice == 3:
            cid = int(input("Enter Customer ID to be Deleted: "))
            sql = "delete from Customer where cid = {}".format(cid)

            ask = input("Are you sure to delete? (yes/no): ")
            if ask == "yes":
                db.write(sql)
                print("[CMS App]", cid, "Deleted from DataBase")
            else:
                print("Delete Operation Skipped")

        elif choice == 4:
            phone = input("Enter Customers Phone Number: ")
            sql = "select * from Customer where phone = '{}'".format(phone)
            rows = db.read(sql)

            columns = ["cid", "name", "phone", "email", "age", "gender", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))

        elif choice == 5:
            cid = int(input("Enter Customers ID: "))
            sql = "select * from Customer where cid = {}".format(cid)
            rows = db.read(sql)

            columns = ["cid", "name", "phone", "email", "age", "gender", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))

        elif choice == 6:
            sql = "select * from Customer"
            rows = db.read(sql)

            columns = ["cid", "name", "phone", "email", "age", "gender", "created_on"]    
            print(tabulate(rows, headers=columns, tablefmt='grid'))
            
            # for row in rows:
            #     print(row)

        elif choice == 0:
            break
        else:
            print("[CMS APP] Invalid Choice", choice)


if __name__ == "__main__":
    main()
