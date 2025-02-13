username = input("set your username:")
password = input("set your password:")
print ("Please sign in ")

input_username =input("Enter username:")
input_password =input("Enter password:")
if input_username == username and input_password == password:
    print("Access granted!")
    print("Welcome to the system")
else:print("Access denied!")
exit()