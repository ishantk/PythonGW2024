# Promo Code: ZOMATO
# Condition1: more than 249
# Condition2: 50% Off upto 150

amount = float(input("Enter Amount: "))
promo_code = input("Enter Promo Code: ")

# Nested if/else
if promo_code == "ZOMATO":
    print("Promo Code Valid")

    if amount > 249:
        print("Promo Code ZOMATO applied...")

        discount = 0.50 * amount

        if discount >= 150:
            discount = 150

        amount -= discount
        print("Discount:", discount)
        print("Please Pay:", amount)

    else:
        print("Amount is Low...")

else:
    print("Promo Code Invalid")