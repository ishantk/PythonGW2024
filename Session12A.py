# Dish: name, price, rating

class Dish:

    def __init__(self, name="", price=0, rating=1.5):
          self.name = name
          self.price = price
          self.rating = rating

    def show(self):
        print("--------Dish--------")
        print("{} | {} | {}".format(self.name, self.price, self.rating))
        print("--------------------")


# Outside the class
def bubble_sort(data):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j].price > data[j+1].price:
            # if data[j].rating < data[j+1].rating:
                # Swap Operation
                data[j], data[j+1] = data[j+1], data[j]

# HW: Implement different sorting techniques on List of Dishes
# List of Dish Objects

"""
dish1 = Dish(name="Dal Makhani", price=250, rating=4.5)
dish2 = Dish(name="Paneer Makhani", price=400, rating=4.2)
dish3 = Dish(name="Noodles", price=300, rating=3.5)
dish4 = Dish(name="Pizza", price=650, rating=4.0)
dish5 = Dish(name="Burger", price=50, rating=3.1)
# dishes = [dish1, dish2, dish3, dish4, dish5]
"""

dishes = [
          Dish(name="Dal Makhani", price=250, rating=4.5), 
          Dish(name="Paneer Makhani", price=400, rating=4.2), 
          Dish(name="Noodles", price=300, rating=3.5), 
          Dish(name="Pizza", price=650, rating=4.0), 
          Dish(name="Burger", price=50, rating=3.1)
          ]

# for idx in range(len(dishes)):
#      dishes[idx].show()
print("DISHES:")
for dish in dishes:
     dish.show()

bubble_sort(dishes)


print("SORTED DISHES:")
for dish in dishes:
     dish.show()