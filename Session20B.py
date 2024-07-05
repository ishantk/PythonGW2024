# Strings are IMMUTABLE -> THEY CANNOT BE CHANGED

quote = "be exceptional"
print("HashCode of quote is:", id(quote))
s1 = quote.upper()
print("1. Quote is:", quote)
print("1. HashCode of quote is:", id(quote))

s2 = quote.lower()
print("2. Quote is:", quote)
print("2. HashCode of quote is:", id(quote))

print("s1 is:", s1)
print("s2 is:", s2)

s3 = quote.capitalize()
print("s3 is:", s3)

s4 = quote.title()
print("s4 is:", s4)

quote = "Be Exceptional"
s5 = quote.swapcase()
print("s5 is:", s5)
