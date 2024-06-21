class Customer:

    def __init__(self, name="", phone="", email="", address=""):
          self.name = name
          self.phone = phone
          self.email = email
          self.address = address

    def show(self):
        print("--------Customer--------")
        print("{} | {}".format(self.name, self.phone))
        print("{} | {}".format(self.email, self.address))
        print("------------------------")

