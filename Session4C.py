# Condition1: Amount should be greater than 500

promo_code = "GET200"
min_amount = 500

amount = float(input("Enter Your Amount: "))

# Conditional Construct : if/else
if amount > min_amount:
    print("You can apply promo code", promo_code)
    # amount = amount - 200
    amount -= 200
    print("Promo Code Applied Successfully. Please pay:", amount)
else:
    print("You cannot apply promo code", promo_code)
    print("Add Items worth", (min_amount-amount), "more..")