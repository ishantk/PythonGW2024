name = input("Enter Customer Name: ")
phone = input("Enter Customer Phone: ")
email = input("Enter Customer Email: ")

customer_details = "{},{},{}\n".format(name, phone, email)

# file = open("/Users/ishant/Downloads/customers.csv", "a")
file = open("customers.csv", "a")
file.write(customer_details)
print("Customer Data Saved..")
file.close()