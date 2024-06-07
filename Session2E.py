# Add to Cart

cart = []
quantity = []
price = []

menu = {
    "burger": 100,
    "noodles": 200,
    "pizza": 300,
    "samosa": 50,
    "momos": 60
}

print("~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to Foodies...")
print("~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Food Menu")
print(menu)
print("~~~~~~~~~~~~~~~~~~~~~~~\n")

while True:
    item = input("Enter Food Item to add in cart or 0 to quit: ")
    
    if item == "0":
        break
    
    qty = int(input("Enter Quantity for item: "))
    quantity.append(qty)

    cart.append(item)
    price.append(menu[item]*qty)

print("CART is:")
print(cart)
print("QUANTITY:")
print(quantity)
print("PRICES are:")
print(price)
print("Items in Cart:", len(cart))
print("Amount to Pay: ", sum(price))