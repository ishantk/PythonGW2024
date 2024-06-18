"""
    Code 3 Objects
    1. Dish : name, price, rating
    2. Menu : name, number_of_dishes, menu_dishes 
        1 Menu can have many Dishes (1 to many)
    3. Restaurant : name, phone, email, address, operating_hours, ratings, menu
        1 Restaurant can have 1 Meny (1 to 1)

"""

# from Session9 import Dish

class Menu:

    def __init__(self, name="NA", number_of_dishes=0, menu_dishes=[]):
        self.name = name
        self.number_of_dishes = number_of_dishes
        self.menu_dishes = menu_dishes

    def show(self):
        print("MENU:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Menu: {} | {}".format(self.name, self.number_of_dishes))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        print("DISHES:")
        for idx in range(len(self.menu_dishes)):
            self.menu_dishes[idx].show()

"""
dishes = [
        Dish(), 
        Dish("Dal Makhani", 250, 4.5),
        Dish(name="Paneer Masala", price=350, rating=4.5)
    ]

menu = Menu(
    name="Indian Veggie Delight", 
    number_of_dishes=len(dishes), 
    menu_dishes=dishes)

menu.show()
"""