username = 'admin'
password = '123456'

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

if username == username_input and password == password_input:
    print("Login successful")
else:
    print("Login failed")

