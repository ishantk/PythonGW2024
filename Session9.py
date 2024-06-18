"""
    Code 3 Objects
    1. Dish : name, price, rating
    2. Menu : name, number_of_dishes, dishes 
        1 Menu can have many Dishes (1 to many)
    3. Restaurant : name, phone, email, address, operating_hours, ratings, menu
        1 Restaurant can have 1 Meny (1 to 1)

"""
# Class for the Object Dish
class Dish:

    # Parameterized Constructor, with default values of arguments passed to it
    def __init__(self, name="NA", price=0, rating=1.5):
        # print(">> self is: {}".format(self))
        # copy the contents of name (input to constructor) into self.name (attribute of object)
        self.name = name 
        self.price = price
        self.rating = rating

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Dish: {} | {} | {}".format(self.name, self.price, self.rating))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


# dish1 = Dish()
# print("dish1:", hex(id(dish1)))

# dish2 = Dish("Dal Makhani", 250, 4.5)
# print("dish2:", hex(id(dish2)))

# dish3 = Dish(name="Paneer Masala", price=350, rating=4.5)
# print("dish2:", hex(id(dish3)))



# List of Dishes
"""
dishes = [
        Dish(), 
        Dish("Dal Makhani", 250, 4.5),
        Dish(name="Paneer Masala", price=350, rating=4.5)
    ]

print("DISHES:\n")
for idx in range(len(dishes)):
    dishes[idx].show()
"""