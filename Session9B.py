"""
    Code 3 Objects
    1. Dish : name, price, rating
    2. Menu : name, number_of_dishes, menu_dishes 
        1 Menu can have many Dishes (1 to many)
    3. Restaurant : name, phone, email, address, operating_hours, ratings, menu
        1 Restaurant can have 1 Meny (1 to 1)

"""

from Session9 import Dish
from Session9A import Menu

class Restaurant:

    def __init__(self, name="NA", phone="NA", email="NA", address="NA", operating_hours="10:00 to 23:00", ratings=2.5, menu=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.operating_hours = operating_hours
        self.ratings = ratings
        self.menu = menu

    def show(self):
        print("RESTAURANT")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Restaurant: {} | {} | {}".format(self.name, self.phone, self.email))
        print("Address: {} | {} | {}".format(self.address, self.operating_hours, self.ratings))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        self.menu.show()
    
"""
dishes = [
        Dish(), 
        Dish("Dal Makhani", 250, 4.5),
        Dish(name="Paneer Masala", price=350, rating=4.5)
    ]
"""

"""
menu = Menu(
    name="Indian Veggie Delight", 
    number_of_dishes=len(dishes), 
    menu_dishes=dishes)
"""

"""
restaurant = Restaurant(name="Ludhiana Veggie Delight",
                        phone="+91 99999 11111",
                        email="veggies@abc.com",
                        address="Krishna Nagar", 
                        ratings=4.5,
                        menu=Menu(
                            name="Indian Veggie Delight", 
                            number_of_dishes=3, 
                            menu_dishes=[
                                        Dish(), 
                                        Dish("Dal Makhani", 250, 4.5),
                                        Dish(name="Paneer Masala", price=350, rating=4.5)
                                    ])
                        )

restaurant.show()
"""

Restaurant(name="Ludhiana Veggie Delight",
                        phone="+91 99999 11111",
                        email="veggies@abc.com",
                        address="Krishna Nagar", 
                        ratings=4.5,
                        menu=Menu(
                            name="Indian Veggie Delight", 
                            number_of_dishes=3, 
                            menu_dishes=[
                                        Dish(), 
                                        Dish("Dal Makhani", 250, 4.5),
                                        Dish(name="Paneer Masala", price=350, rating=4.5)
                                    ])
                        ).show()

Restaurant(name="Ludhiana Veggie Delight",
                        phone="+91 99999 11111",
                        email="veggies@abc.com",
                        address="Krishna Nagar", 
                        ratings=4.5,
                        menu=Menu(
                            name="Indian Veggie Delight", 
                            number_of_dishes=3, 
                            menu_dishes=[
                                        Dish(), 
                                        Dish("Dal Makhani", 250, 4.5),
                                        Dish(name="Paneer Masala", price=350, rating=4.5)
                                    ])
                        ).show()