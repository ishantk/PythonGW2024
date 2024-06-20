from Session11 import Customer

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to Customer Management System")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

while True:

    print("1: Add Customer")
    print("2: View Customers")
    print("0: Quit")

    choice = int(input("Enter Your Choice: "))
    print("You Selected:", choice)

    if choice == 1:
        file = open("customers.csv", "a")
        customer = Customer()
        customer.add_customer_details()
        customer.show()

        data = customer.to_csv()
        file.write(data)
        print("Data Written:", data)
    
    elif choice == 2:
        file = open("customers.csv", "r")
        lines = file.readlines()
        for line in lines:
            print(line)

    elif choice == 0:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Thank You for using Customer Management")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        file.close()
        break
    
