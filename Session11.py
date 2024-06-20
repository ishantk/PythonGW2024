#  Customer: name, phone, email, address, gender, age
class Customer:

    def __init__(self, name="", phone="", 
                 email="", address="", gender="", age=15):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.gender = gender
        self.age = age

    def add_customer_details(self):
        print(">> ENTER CUSTOMER DETAILS")
        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customer Email: ")
        self.address = input("Enter Customer Address: ")
        self.gender = input("Enter Customer Gender: ")
        self.age = int(input("Enter Customer Age: "))


    def show(self):
        print("------------------CUSTOMER-----------------")
        print("Name: {} | Phone: {}".format(self.name, self.phone))
        print("Email: {} | Address: {}".format(self.email, self.address))
        print("Gender: {} | Age: {}".format(self.gender, self.age))
        print("------------------------------------------")

    def to_csv(self):
        # John,+91 98765 12345,john@example.com,Redwood Shores,male,32
        data = "{},{},{},{},{},{}\n".format(self.name, 
                                            self.phone, self.email, self.address, self.gender, self.age)
        return data