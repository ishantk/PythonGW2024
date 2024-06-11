"""
    ZOMATO: 20% off
          : min value: 300

    BINGO: 50% off
         : min value: 500
         : max discount: 100


    # Indentation: PEP (Python Enhancement Proposal)
    # https://peps.python.org/pep-0001/
"""
# if/else -> Workflows

promo_code = input("Enter Promo Code: ")
amount = float(input("Enter Amount: "))

if promo_code == "ZOMATO":
    print("ZOMATO can be applied...")

    if amount > 300:
        discount = 0.20 * amount
        print("ZOMATO Applied Successfully. You goat a discount of:", discount)
        print("You can pay:", amount-discount)
    else:
        print("Amount is Less. Please add items worth ", (300-amount), "more")

elif promo_code == "BINGO":
    print("BINGO can be applied...")

    if amount > 500:
        discount = 0.50 * amount

        if discount > 100:
            discount = 100

        print("BINGO Applied Successfully. You got a discount of:", discount)
        amount -= discount
        amount = amount + 0.18*amount
        amount += 16.5 # delivery fee
        print("You can pay: \u20b9", amount-discount)
    else:
        print("Amount is Less. Please add items worth ", (500-amount), "more")

else:
    print("Invalid Promo Code")

# HW: https://symbl.cc/en/unicode-table/#devanagari
# Write your name in HINDI/PUNJABI/whatever the language you are interested using unicodes