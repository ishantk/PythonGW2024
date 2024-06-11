# Linear Search

instagram_user_names = ["john.j", "fionna", "harry_h", "leo.32", "ben_a"]
names = ["John Jackson", "Fionna Flynn", "Harrison", "Leonardo", "Bennethan"]

user_name = input("Enter User Name to Search: ")


"""

# Below approach is wrong:
# As we are coding too much on lot of data
idx = 0

if user_name == instagram_user_names[idx]:
    print("NAME IS:", names[idx])
elif user_name == instagram_user_names[idx+1]:
    print("NAME IS:", names[idx+1])
elif user_name == instagram_user_names[idx+2]:
    print("NAME IS:", names[idx+2])
elif user_name == instagram_user_names[idx+3]:
    print("NAME IS:", names[idx+3])
elif user_name == instagram_user_names[idx+4]:
    print("NAME IS:", names[idx+4])
else:
    print("Cannot Find User")
"""

"""
# While Loop
idx = 0

while idx < len(instagram_user_names):
    
    print("Check", user_name, "with",  instagram_user_names[idx])
    
    if user_name == instagram_user_names[idx]:
         print("NAME IS:", names[idx])
         break
    
    idx+=1
"""

flag = False

for idx in range(0, len(instagram_user_names)): # idx will start from 0 and go till 4
    
    # print("Check", user_name, "with",  instagram_user_names[idx])
    
    if user_name == instagram_user_names[idx]:
         print("NAME IS:", names[idx])
         flag = True
         break
    
if flag == False:
     print(user_name, "Not Found :(")