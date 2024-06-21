"""
    OOPS case Study for the Day. Food Delivery App.
    
    Customer
    Dish
    Order

    1 Customer can place many Orders
    1 Order can have many Dishes

"""

class Dish:

    def __init__(self, name="", price=0, rating=1.5):
          self.name = name
          self.price = price
          self.rating = rating

    def show(self):
        print("--------Dish--------")
        print("{} | {} | {}".format(self.name, self.price, self.rating))
        print("--------------------")


