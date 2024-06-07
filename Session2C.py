# Dictionary - 
# The final and most important and mostly used container in Computer Science
friends = {"jj": "john", "je": "jennie", "ji":"jim", "ki": "john"}
print(friends, type(friends), id(friends))
print(friends["jj"])

my_friends = {1: "Call", 2:"Message", 3:"Get a CallBack"}

# HW: Draw the RAM Model of Dictionary

instagram = {
    "k_ishant": {"auribises", "john", "jennie", "jim", "fionna"},
    "auribises": {"k_ishant", "george", "sia", "leo", "john"}
}

print(instagram["k_ishant"])
print(instagram["auribises"])

print(instagram["k_ishant"] & instagram["auribises"])
