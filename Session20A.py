# Properties
"""
    Indexing
    Negative Indexing
    Slicing
    Concatenation
    Multiplicity
    Membership Testing
"""

quote = "search the candle rather than cursing the darkness"
print("1. HashCode of Quote:", id(quote))

print(quote[1])
print(quote[-1])
print(quote[-8:])

quote = quote + "\n" + "Be Exceptional\n"
print(quote)
print("2. HashCode of Quote:", id(quote))

data = quote * 3
print("`````````````````")
print(data)
print("`````````````````")

print("the" in quote)

email = input("Enter Your Email: ")
if "@" in email and "." in email:
    print("Email is Well Formed:", email)
else:
    print("Email is NOT Well Formed:", email)


contacts = ["john", "jennie", "kia", "joe", "jackson", "anna", "sia"]
search = input("Enter Search keyword: ")
for contact in contacts:
    if search in contact:
        print(contact)